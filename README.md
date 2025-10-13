# P2P Network Project

A simple peer-to-peer network implementation for distributed systems.

## Features

- Decentralized peer discovery
- Direct peer-to-peer communication
- Message broadcastinga
- Automatic peer reconnection

## Prerequisites

- Node.js (v16 or higher)
- npm or yarn

## Installation

```bash
npm install
# or
yarn install
```

## Usage

1. Start a peer node:
```bash
npm start
# or
yarn start
```

2. Connect to other peers by providing their address:
```bash
npm start -- --connect <peer-address>
```

## Configuration

You can configure the following parameters in `config.json`:
- Port number
- Bootstrap nodes
- Connection timeout
- Maximum peers

## Contributing

1. Fork the repository
2. Create your feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License.
