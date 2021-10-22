# filegen

Generate and send a large-ish file to the user. A simple way to speed-test.

Currently hosted @ https://filegen.arunsr.in

# Setup and run

```sh
./run.sh
```

# Usage

```sh
curl localhost:8000/size/1 > /dev/null
  <- returns a 1mb file
curl localhost:8000/size/10 > /dev/null
  <- returns a 10mb file
```
