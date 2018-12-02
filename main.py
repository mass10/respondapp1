#!/usr/bin/env python3
# coding: utf-8
import responder

api = responder.API()

@api.route("/{greeting}")
async def greet_world(req, res, *, greeting):
	res.text = f"{greeting}, world!"

def main():
	api.run()

main()
