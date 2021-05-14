# AWS - lambda with container

## How to Run Script in Container
app.pyの編集を反映させるためには毎回buildが必要（だと思う）
### 面倒くさい方法
1. for dev
```bash
# build image
$ docker build -t {image name} .

# start container
$ docker run --rm -p 9000:8080 {image name} -v $HOME/.aws/:/root/.aws/
```
2. run lambda
```bash
curl -d '{}' http://localhost:9000/2015-03-31/functions/function/invocations
```

### 面倒くさくない方法(compose)
1. build image & run
```bash
$ docker-compose up --build
```

2. run lambda
```bash
curl -d '{}' http://localhost:9000/2015-03-31/functions/function/invocations
```

## USE environment variables
1. edit .env file
2. build image
3. run lambda
