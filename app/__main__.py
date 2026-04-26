#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# app/__main__.py

"""A simple Flask Restful API for getting information about Minecraft servers.
Works with Java and Bedrock servers.
"""
import os
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT", '3000'))
