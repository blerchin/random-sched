# Random Schedule Generator

This is a quick script that randomly assigns a group of people to a set of time slots.

### Usage:

*Tested with python3, but should work fine on 2.7*

```
git clone https://github.com/blerchin/random-sched.git

pip3 install -r requirements.txt
./shuffle.py
```

To define your dates and names, edit `data.yml`.
`people` should be a list of names, and `dates` should be a list of timeslots. Really, these can contain any string.

`dates` are filled from top to bottom. If there are more `people` than dates, some will be ignored. If there are more dates than people, the remaining slots will be assigned to 'None'.
