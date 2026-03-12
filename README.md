<h1>
  <img src="./website/src/assets/icon.svg" width="50" style="vertical-align:middle">
  LEIC GitHub Leaderboard
</h1>

---

LEIC GitHub Leaderboard is a website where students from FEUP's LEIC bachelor program are ranked based on their GitHub stats.

Students are ranked based on the formula:

$$ Score =  Stars \times 20 + Commits \times 1 + Pull Requests \times 3.5 + Repos \times 1 + Followers \times 1 $$ 

Which is meant to value good contributions more, but still reward hard working students. Improvement suggestions are welcome!

## FAQ

### I don't want to be on this leaderboard!
If your account is ranked here and you don't want it to be, you can just contact me and I'll remove it right away!

### I want to be on this leaderboard!
As long as you have been a LEIC student at FEUP, you're welcome to join!\n
Just contact me and I'll add you to the leaderboard.

### Where do you get student's GitHubs from?
The list of student's GitHub usernames comes from:
- The members of some GitHub organizations created for some classes.
- Public spreadsheets from some classes.
- Manually adding some people.

### When are scores updated?
Scores are updated once a week, at 00:00 Sunday UTC, through a GitHub action.\n
You can check when it was last updated in the top right corner.\n
You can also check the status of the last fetch in the [GitHub action page](https://github.com/Mews/leic-gh-leaderboard/actions/workflows/update.yaml).

### Do private contributions count?
Student data is fetched using GitHub's GraphQL api, which *usually* cannot see private repos / contributions.\n
So no, private contributions usually aren't counted, with some exceptions, like if you specifically make them visible.

### Which repos count towards my stats?
Currently, only repos that you are the owner of are counted towards your stats on the leaderboard, though this
might change in the future.
