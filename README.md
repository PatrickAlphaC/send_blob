# send-blob

- [send-blob](#send-blob)
- [About](#about)
  - [What are blobs?](#what-are-blobs)
- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Quickstart](#quickstart)
  - [Using pip](#using-pip)
- [Example Blob transactions:](#example-blob-transactions)
- [Acknowledgements](#acknowledgements)


# About

## What are blobs?

BLObs or "Binary Large Objects" are a way to store large amounts of data on the blockchain. In this repo, we show how to send a blob. Keep in mind, that all blobs *must* be at least 4,096 words in length, with each word being 32 bytes long. Aka, at least 131,072 bytes.

So there is no "small blob".

# Getting Started

## Requirements
- [python](https://www.python.org/downloads/)
  - You'll known you've installed it correctly if you can run `python --version` in your terminal and see an output like `Python 3.12.2`.
- [rye](https://rye-up.com/guide/installation/)
  - You'll know you've installed it correctly if you can run `rye --version` in your terminal and see an output like
```
rye 0.32.0
commit: 0.32.0 (e1b4f2a29 2024-03-29)
platform: macos (x86_64)
self-python: cpython@3.12.2
symlink support: true
uv enabled: true
```
- [anvil (foundry)](https://book.getfoundry.sh/getting-started/installation)
  - You'll know you've installed it correctly if you can run `anvil --version` in your terminal and see an output like `anvil 0.2.0 (4aa17bc 2024-05-14T00:17:46.920053000Z)`

## Installation

We use rye to manage our project dependencies. There are optional instructions for just using `pip` to install and run as well. 

```bash
git clone https://github.com/PatrickAlphaC/send_blob
cd send_blob
rye sync
```

## Quickstart

Setup an anvil locally running chain.

```bash
anvil 
```

Then, execute the blob script. 
```bash
rye run send-blob
```

You'll get 2 distinct outputs printed to your terminal.

1. The first will be the signed transaction. You can use this to manaullay learn how to send a curl blob transaction.
2. The second will be a transaction receipt

## Using pip

Optionally, you can use pip to install the dependencies and run the project.

```bash
pip install -r requirements-dev.lock
```

# Example Blob transactions:

- [zkSync blob commitment](https://etherscan.io/tx/0x291351476ef62e83ed33fb385f998232b8577bd1af60eb3463ce5a9e77fc8666)

# Acknowledgements
- [fselmo](https://github.com/fselmo) (for helping me send a blob tx with web3py)