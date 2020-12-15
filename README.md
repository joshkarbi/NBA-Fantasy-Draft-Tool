# About
Small tool to help rank which players to draft based on a configurable strategy.
Takes last season's stats for every active player, then gives each player a score for this season based on weightings
specified in a strategy. Higher weights should be given to categories active in your league.

# Dependencies
basketball_reference_web_scraper, see https://pypi.org/project/basketball-reference-web-scraper/
ipython widgets

# Running
```bash
jupyter nbextension enable --py widgetsnbextension
jupyter-notebook
```

Use the notebook to scrape data, configure strategy, and draft players.
During each drafting round, either:
- Select "My Pick" then hit "Submit" to get a draft recommendation,
or
- Select "Others Pick", enter the name (or beginning of the name) of the player drafted, then hit submit to remove player from the available set

# Areas for improvement
There are clear downfalls to this approach:
1. It completely ignores rookies.
2. It ignores players who were out last season.
3. It may underestimate players who are now on a different team, where they may play better.
4. It is based on data from only last season.

This tool can be improved by also using data from previous seasons by:
 - Simulating player performance based on range of potential results for next season (ie. a normal distribution)
 - Assuming an average of previous stats
 - Predicting next season stats by assuming a trendline continues into the future

The tool can also be improved by using data from the NBA draft in between seasons and weighting the draft order as part of player scores.
