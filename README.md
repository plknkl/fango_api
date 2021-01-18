# Fango REST

`docker-compose up` runs containers, with rest container on `localhost:5000`

## Shows

### Get list of shows

`GET /shows`

### Response
```
[
  {
    "id": 12,
    "title": "Bathysphere",
    "description": "Una fumosa deep-immersion tra le ultime uscite, senza distinzione alcuna di origine o genere.",
    "bio": "Leo per tutti, Cianfa per molti, vivo di musica in A Buzz Supreme.",
    "image": "https://www.fangoradio.com/shows/bathysphere/bathysphere.jpg",
    "tags": [
      "newreleases",
      "alternative"
    ]
  },
  {
    "id": 13,
    "title": "Dub & Culture",
    "description": "Proprio come una vecchia trasmissione radio: due piatti, un mixer e un microfono, album e singoli in vinile, il Dub e la sua storia… Ecco cosa vi aspetta nel programma del veterano del dub italiano Rankin Alpha, che ci racconterà aneddoti e storie più o meno (o per niente) conosciute del dub e della sua favolosa storia.",
    "bio": "Rankin Alpha: polistrumentista, produttore, cantante.",
    "image": "https://www.fangoradio.com/shows/dub-and-culture/dub-and-culture.jpg",
    "tags": [
      "dub",
      "monography"
    ]
  }
]
```


### Add / modify a show

`POST /shows`

```
{
  "bio": "Punk Alpha: polistrumentista, produttore, cantante.",
  "description": "Proprio come una vecchia trasmissione radio: due piatti, un mixer e un microfono, album e singoli in vinile, il Dub e la sua storia… Ecco cosa vi aspetta nel programma del veterano del dub italiano Rankin Alpha, che ci racconterà aneddoti e storie più o meno (o per niente) conosciute del dub e della sua favolosa storia.",
  "id": 13,
  "image": "https://www.fangoradio.com/shows/dub-and-culture/dub-and-culture.jpg",
  "tags": [
    "dub",
    "monography"
  ],
  "title": "Dub & Culture"
}
```

### Response
```
{
  "bio": "Punk Alpha: polistrumentista, produttore, cantante.",
  "description": "Proprio come una vecchia trasmissione radio: due piatti, un mixer e un microfono, album e singoli in vinile, il Dub e la sua storia… Ecco cosa vi aspetta nel programma del veterano del dub italiano Rankin Alpha, che ci racconterà aneddoti e storie più o meno (o per niente) conosciute del dub e della sua favolosa storia.",
  "id": 13,
  "image": "https://www.fangoradio.com/shows/dub-and-culture/dub-and-culture.jpg",
  "tags": [
    "dub",
    "monography"
  ],
  "title": "Dub & Culture"
}
```


### Delete a show

`DELETE /shows/12`

### Response
```
{
  "result": "12 deleted"
}
```



## Episodes

### Get list of episodes
The episodes could be loaded only providing a `show id`.

`GET /shows/1/episodes`

### Response
```
[
  {
    "id": 1,
    "show_id": 12,
    "title": "Episode 1",
    "description": "The very first episode",
    "image": "https://www.fangoradio.com/shows/bathysphere/bathysphere.jpg",
    "tracklist": [
      {
        "title": "Michael Dorn",
        "starts_at": "00:00:00",
        "ends_at": "00:01:30"
      },
      {
        "title": "James Holden",
        "starts_at": "00:01:30",
        "ends_at": "00:10:00"
      }
    ]
  },
  {
    "id": 2,
    "show_id": 12,
    "title": "Episode 2",
    "description": "The second best episode",
    "image": "https://www.fangoradio.com/shows/bathysphere/bathysphere.jpg",
    "tracklist": []
  }
]
```


### Add / modify an episode

`POST /episodes`

```
{
    "description": "The really first episode",
    "id": 1,
    "image": "https://www.fangoradio.com/shows/bathysphere/bathysphere.jpg",
    "show_id": 12,
    "title": "Episode 1",
    "tracklist": [
      {
        "ends_at": "00:01:30",
        "starts_at": "00:00:00",
        "title": "Michael Dorn"
      },
      {
        "ends_at": "00:10:00",
        "starts_at": "00:01:30",
        "title": "James Holden"
      }
		]
}
```

### Response
```
{
    "description": "The really first episode",
    "id": 1,
    "image": "https://www.fangoradio.com/shows/bathysphere/bathysphere.jpg",
    "show_id": 12,
    "title": "Episode 1",
    "tracklist": [
      {
        "ends_at": "00:01:30",
        "starts_at": "00:00:00",
        "title": "Michael Dorn"
      },
      {
        "ends_at": "00:10:00",
        "starts_at": "00:01:30",
        "title": "James Holden"
      }
		]
}
```


### Delete an episode

`DELETE episodes/2`

### Response
```
{
  "result": "2 deleted"
}
```



## Utility
Utility endpoints for administration needs

### Reset Database

`POST /reset`

```
{
	"password": "fangopass"
}
```

### Response
```
{
  "result": "all clear"
}
```


### Load dummies

`POST /load-dummy`

```
{
	"password": "fangopass"
}
```

### Response
```
{
  "result": "dummy loaded"
}
```