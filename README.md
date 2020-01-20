# Client

```
> cd client
> npm install
> npm run build
```

把 `/client/build/` 內容移動到 `/app/static/` ，格式如下。

```
app/
    static/
        css/
        js/
        ...
        index.html
        robots.txt
        ...
```

# Server

- 安裝 [Python 3.8](https://www.python.org/downloads/)
- 安裝 `pipenv`
    - `pip install pipenv`
- 安裝專案相依
    - `pipenv install --dev`
- `pipenv shell`
- `python moo.py`