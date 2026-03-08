The `fetch.py` script requires the following environment variables to be set
- GITHUB_TOKEN - A GitHub personal access token to access the GraphQL api.
- OUTPUT_FOLDER - The path to store the data
- QUERY_BATCH_SIZE - How many users to fetch in each query. This can be lowered if for any reason a batch is too big and denied by GitHub

It will then create two files in OUTPUT_FOLDER. `userdata.json`, with the fetched github data, and `querydata.json`, with some data about the fetch, like the date and how many users were stored.

The `fetch.py` script will run periodically (once a week) from a GitHub action and update the data for the website to use.

Stars are considered only for repositories where the user is either an owner or a collaborator.

The fetch script currently can only aggregate the stars from the first 100 repos on a user's account. This is a limitation of GitHub's GraphQL api, and it can be solved in the future by using pagination.

Only commits from the last 365 days are counted.

Data returned by the GraphQL query might look something like this:
```json
{
   "data":{
      "u0":{
         "login":"AlexandreNogueira202404206",
         "followers":{
            "totalCount":0
         },
         "ownRepos":{
            "totalCount":1,
            "totalStargazers":[
               {
                  "stargazerCount":0
               }
            ]
         },
         "collaboratorRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "pullRequests":{
            "totalCount":0
         },
         "contributionsCollection":{
            "totalCommitContributions":0
         }
      },
      "u1":{
         "login":"AnaRodrigues-202405140",
         "followers":{
            "totalCount":0
         },
         "ownRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "collaboratorRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "pullRequests":{
            "totalCount":0
         },
         "contributionsCollection":{
            "totalCommitContributions":0
         }
      },
      "u2":{
         "login":"leonor1306",
         "followers":{
            "totalCount":0
         },
         "ownRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "collaboratorRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "pullRequests":{
            "totalCount":0
         },
         "contributionsCollection":{
            "totalCommitContributions":0
         }
      },
      "u3":{
         "login":"PeterF521",
         "followers":{
            "totalCount":1
         },
         "ownRepos":{
            "totalCount":14,
            "totalStargazers":[
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               },
               {
                  "stargazerCount":0
               }
            ]
         },
         "collaboratorRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "pullRequests":{
            "totalCount":7
         },
         "contributionsCollection":{
            "totalCommitContributions":2
         }
      },
      "u4":{
         "login":"Jose-Maio",
         "followers":{
            "totalCount":0
         },
         "ownRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "collaboratorRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "pullRequests":{
            "totalCount":0
         },
         "contributionsCollection":{
            "totalCommitContributions":0
         }
      },
      "u5":{
         "login":"m1ke26",
         "followers":{
            "totalCount":2
         },
         "ownRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "collaboratorRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "pullRequests":{
            "totalCount":0
         },
         "contributionsCollection":{
            "totalCommitContributions":0
         }
      },
      "u6":{
         "login":"VascoGuimaraes",
         "followers":{
            "totalCount":0
         },
         "ownRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "collaboratorRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "pullRequests":{
            "totalCount":0
         },
         "contributionsCollection":{
            "totalCommitContributions":0
         }
      },
      "u7":{
         "login":"Victorg2705",
         "followers":{
            "totalCount":0
         },
         "ownRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "collaboratorRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "pullRequests":{
            "totalCount":0
         },
         "contributionsCollection":{
            "totalCommitContributions":0
         }
      },
      "u8":{
         "login":"riqui07",
         "followers":{
            "totalCount":0
         },
         "ownRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "collaboratorRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "pullRequests":{
            "totalCount":0
         },
         "contributionsCollection":{
            "totalCommitContributions":0
         }
      },
      "u9":{
         "login":"monteirou",
         "followers":{
            "totalCount":0
         },
         "ownRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "collaboratorRepos":{
            "totalCount":0,
            "totalStargazers":[
               
            ]
         },
         "pullRequests":{
            "totalCount":0
         },
         "contributionsCollection":{
            "totalCommitContributions":0
         }
      }
   }
}
```
