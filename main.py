#!/usr/bin/env python3
# coding: utf-8
#
#
#
#
#   pip3 install responder
#
#
#
#

import sys
import responder

api = responder.API()

#
# routings:
#   上から順に適用されます。
#

@api.route("/hello/{name}")
async def greet_world(req, res, *, name):
	res.text = f"welcome, {name}."

@api.route("/{greeting}")
async def greet_world(req, res, *, greeting):
	res.text = f"{greeting}, world!"

def main(argv):
	argv = argv[1:]
	api.run(address="0.0.0.0", port=8080)

main(sys.argv)
