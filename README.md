# Serverless

Playing around with the Serverless Framework

## Quick start

```shell
git clone https://github.com/freddywordingham/serverless.git
cd serverless
```

## Requirements

- [Node.js](https://nodejs.org/en/)

```shell
brew install node
```

## Setup

Install dependencies:

```shell
npm install
```

## Development

Start serverless offline:

```shell
serverless offline
```

And configure the `.env` file to point to the local server:

```shell
SERVERLESS_ENDPOINT=http://localhost:3002
```

Then run the scripts in `tests/` to test the endpoints:

```shell
python tests/hello.py
```

## Commands

Deploy:

```shell
serverless deploy
```

Invoke a deployed function from `Python` by configuring the `.env` file:

```shell
SERVERLESS_ENDPOINT=<endpoint_url>
```

Remove deployment:

```shell
serverless remove
```
