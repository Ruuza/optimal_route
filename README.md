# optimal_route
Interview task


## Task

### Task: Calculate optimal route for Wattstor engineer

### Description:
Wattstor engineer needs to visit a couple of sites to do routine maintenance.
Please calculate the optimal route, so each site is visited only once and the engineer returns
to the start location.
Each city has attached coordinates GPS (WGS84).
### Input:
Following is list of cities with their coordinates, start and end is in Brno
- Brno 49.19564, 16.60895
- Jihlava 49.39933, 15.58344
- Prague 50.08144, 14.424088
- Beroun 49.964855, 14.07005
- Hradec Kralove 50.20604, 15.83271

### Expected output:
List of cities ordered by optimal route with calculated distances and total distance.
Please write code in Python 3, use OOP, if possible write unit tests.
Code needs to be executed from the command line, as a parameter accepting JSON input
file, as output displaying the result on screen (to keep things simple list can be max 5 or
strictly 5 items).
Please store code in the GIT repository and share access. You are allowed to use third party
packages if needed.

## How to run

    Python 3.10 is required!

### 1. Install requirements

    pip install -r requirements.txt

### 2. Create the JSON file that defines the cities

example:

```json
{
    "Brno": [
        49.19564,
        16.60895
    ],
    "Jihlava": [
        49.39933,
        15.58344
    ],
    "Prague": [
        50.08144,
        14.424088
    ],
    "Beroun": [
        49.964855,
        14.07005
    ],
    "Hradec Kralove": [
        50.20604,
        15.83271
    ]
}
```

### 3. Run the program

    python optimal_route.py -i <cityfile.json>


note: Use `python optimal_route.py -h` for help


## Run the tests

to run the automatic tests, run:

    pytest