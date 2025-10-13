# P2P Network Project
•	This project is a peer-to-peer (P2P) tutoring system designed for students. It allows students to connect directly with each other without relying on a central server. The system includes features such as decentralized peer discovery, enabling students to find and connect with other peers automatically. Once connected, students can communicate directly, share messages, and meet on live rooms to tutor. Additionally, the system ensures that if a student disconnects, they can automatically reconnect, maintaining a stable and reliable network for collaborative learning and tutoring

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
