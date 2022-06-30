#!/usr/bin/env python3
# ~/bin/libs/globals.py
from globals import RichWrapper
from query import QueryCli

rw = RichWrapper()
rw.outhr()
rw.outbox("Running a query")

query = "SELECT * FROM public.businesses_clients limit 10"

QueryCli("-v", query).process()


anObject = QueryCli("-v", query).process_to_object()

print("Row 0, column client_name")
print(anObject[0].get("client_name"))

rw.outhr()
rw.outbox("Query done")

