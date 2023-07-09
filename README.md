# Public Toilets API

This service provides details of public toilet locations in Plymouth, UK

## API Endpoint
* https://public-toilets.api.smartplymouth.org/

## API Routes
### /toilets
Returns a list of public toilets.

#### Example Request
```curl 'https://public-toilets.api.smartplymouth.org/toilets' | jq```

#### Example Response
```
{
  "last_updated": "2023-07-05T17:15:00Z",
  "toilets": [
    {
      "address": "Armada Way, City Centre, PL1 1HH",
      "attributes": [
        "Disabled",
        "RADAR Key",
        "Baby Change"
      ],
      "fee": "£0.50",
      "id": "82513ed3-5cc6-4ab9-9fdb-79354a9dcab2",
      "latitude": -4.14246,
      "longitude": 50.37156,
      "name": "Armada Way",
      "opening_hours": {
        "fri": {
          "close": "18:00",
          "open": "08:00"
        },
        "mon": {
          "close": "18:00",
          "open": "08:00"
        },
        "sat": {
          "close": "18:00",
          "open": "08:00"
        },
        "sun": {
          "close": "18:00",
          "open": "08:00"
        },
        "thu": {
          "close": "18:00",
          "open": "08:00"
        },
        "tue": {
          "close": "18:00",
          "open": "08:00"
        },
        "wed": {
          "close": "18:00",
          "open": "08:00"
        }
      },
      "operator": "Plymouth City Council"
    },
    {},
    {},
    ...
  ]
}
```

### /toilets/<toilet_id>
Returns information relating to a given public toilet.

#### Example Request
```curl 'https://public-toilets.api.smartplymouth.org/toilets/94bbea4f-3880-4da8-bc4c-3d0feeb7f940' | jq```

#### Example Response
```
{
  "address": "Freedom Park, Lipson, PL4 8QF",
  "attributes": [
    "Disabled",
    "Baby Change"
  ],
  "fee": "unknown",
  "id": "94bbea4f-3880-4da8-bc4c-3d0feeb7f940",
  "latitude": -4.12737,
  "longitude": 50.37827,
  "name": "Freedom Park",
  "opening_hours": {
    "fri": {
      "close": "18:00",
      "open": "08:00"
    },
    "mon": {
      "close": "18:00",
      "open": "08:00"
    },
    "sat": {
      "close": "18:00",
      "open": "08:00"
    },
    "sun": {
      "close": "18:00",
      "open": "08:00"
    },
    "thu": {
      "close": "18:00",
      "open": "08:00"
    },
    "tue": {
      "close": "18:00",
      "open": "08:00"
    },
    "wed": {
      "close": "18:00",
      "open": "08:00"
    }
  },
  "operator": "Plymouth City Council"
}
```

