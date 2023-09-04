# Background

Since Logistically sells software for logistics, our challenge will pertain to that space. One feature of our platform is the ability for our users to quote one or more pallets of freight from one or more trucking companies, aka “carriers”. These carriers will provide quotes to ship freight from point A to point B.

An engineering challenge for Logistically is how to return the best rates from multiple carriers to provide quotes for a customer in a timely manner. The "best rate" could be one or a combination of the following:

1. Lowest cost
2. Quickest delivery date/time

We have simplified this problem so you can complete this challenge in a couple of hours.

# Backend Challenge

You have two (2) hours to provide a solution to the following challenge.

There are two API endpoints that return JSON:

- https://ly-code-challenge.vercel.app/api/carriers
- https://ly-code-challenge.vercel.app/api/rate-quotes/{carrier_code}

`api/carriers` mimics a request to get the list of carriers who are providing quotes.

`api/rate-quotes/{carrier_code}` will require _multiple_ requests/responses with quotes by carrier code.

Some carriers return rate quotes in a couple of seconds, but some could take up to 30 seconds! Some have errors.

Print a list of rate quotes for the carriers to the console. You may pick whatever languages or libraries you feel comfortable using. It should run on Mac or Linux. Print to the console/stdout.

## Basic Requirements

- Call GET `api/carriers` to return a list of carriers to get quotes.
- Then call GET `api/rate-quotes/{carrier_code}` to return a quote for each carrier code.
- Gather a list of quotes.
- Order quotes by `lowest_cost` descending.
- Print the list of quotes for all carriers.

### Notes

- Please show your progress by making small commits along the way. That is, commit changes every few minutes as you work through your solution.
- A solution with incomplete basic requirements is not a failure. Please submit the incomplete solution. We will consider a nice attempt even if it doesn't complete the requirements.

## Bonus Requirements

- Log an error if a rate quote takes longer than 8 seconds.
- Write tests.
- Output the list of quotes as JSON.

# General Guidelines

You have two (2) hours to complete the challenge. Take shortcuts. You can go back and make improvements once it is working.

The solution will be assessed on the working program, code clarity, data modeling, and comments/documentation.
