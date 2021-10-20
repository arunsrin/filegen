# filegen
generate and send a large-ish file to the user

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
