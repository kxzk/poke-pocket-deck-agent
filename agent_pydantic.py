#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import os
from dataclasses import dataclass

from httpx import AsyncClient
from pydantic_ai import Agent, RunContext

from helpers import *


@dataclass
class Deps:
    client: AsyncClient
    anthropic_api_key: str | None


def get_sys_prompt() -> str:
    with open("system_prompt.txt", "r") as f:
        sys_prompt = f.read()
    return sys_prompt


a = Agent(
    "anthropic:claude-3-7-sonnet-latest",
    system_prompt=get_sys_prompt(),
    deps_type=Deps,
)


@a.tool
async def _get_card_data(ctx: RunContext[Deps], card_id: str) -> str:
    print(f"getting_card_id={card_id}")
    d = get_card_data(card_id)
    print(f"got_data={d}")
    return d


@a.tool
async def _get_all_card_ids(ctx: RunContext[Deps]) -> list[dict[str, str]]:
    print("fetching all card ids...")
    return get_all_card_ids()


@a.tool
async def _get_energy_mappings(ctx: RunContext[Deps]) -> str:
    return get_energy_mappings()


async def main():
    async with AsyncClient() as client:
        anthropic_api_key = os.environ["ANTHROPIC_API_KEY"]
        deps = Deps(client=client, anthropic_api_key=anthropic_api_key)

        result = await a.run("Does garchomp have any abilities?", deps=deps)

        print(result.data)


if __name__ == "__main__":
    asyncio.run(main())
