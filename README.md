<h1>
  <img src="./website/src/assets/icon.svg" width="50" style="vertical-align:middle">
  LEIC GitHub Leaderboard
</h1>

LEIC GitHub Leaderboard is a website where students from FEUP's LEIC bachelor program are ranked based on their GitHub stats.

> [!NOTE]
> This is not meant to be an accessment of how good a student is
> 
> It's all just for fun :)

# FAQ

## I don't want to be on this leaderboard!
If your account is ranked here and you don't want it to be, you can just contact me and I'll remove it right away!

You can reach out through discord (mews75) or email (ar754456@gmail.com)

## I want to be on this leaderboard!
As long as you have been a LEIC student at FEUP, you're welcome to join!

Just contact me and I'll add you to the leaderboard.

## How are scores calculated?
Each student's score is calculated according to this formula:

$$Score =  Stars × 20 + Commits × 1 + Pull Requests × 3.5 + Repos × 1 + Followers × 1$$

Ties are then broken using stars, prs, commits, followers, repos, and username (lexicographical order) in that order.

The coefficients are somewhat arbitrarily chosen, but the goal is to value high value contributions more.
Improvement suggestions are welcome!

## Where do you get student's GitHubs from?
The list of student's GitHub usernames comes from:
- The members of some GitHub organizations created for some classes.
- Public spreadsheets from some classes.
- Manually adding some people.

## When are scores updated?
Scores are updated once a week, at 00:00 Sunday UTC, through a GitHub action.

You can check when it was last updated in the top right corner.

You can also check the status of the last fetch in the [GitHub action page](https://github.com/Mews/leic-gh-leaderboard/actions/workflows/update.yaml).

## Do private contributions count?
Student data is fetched using GitHub's GraphQL api, which *usually* cannot see private repos / contributions.

So no, private contributions usually aren't counted, with some exceptions, like if you specifically make them visible.

## Which repos count towards my stats?
Currently, only repos that you are the owner of are counted towards your stats on the leaderboard, though this
might change in the future.
