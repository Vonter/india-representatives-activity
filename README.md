# india-representatives-activity

Dataset of legislative activity by Indian parliamentary representatives. Sourced from [PRS India](https://prsindia.org/).

Browse the minified dataset for the current Lok Sabha here: <https://flatgithub.com/Vonter/india-representatives-activity?filename=csv/Lok%20Sabha/17th.csv&stickyColumnName=Name>.

## Dataset

The complete dataset is available as JSON files under the [json/](json) folder in this repository. The JSON files include details on Attendance, Debates, Questions and Private Member Bills. Each Lok Sabha is available as a separate JSON file:
- [17th Lok Sabha (Current)](json/Lok%20Sabha/17th.json?raw=1)
- [16th Lok Sabha](json/Lok%20Sabha/16th.json?raw=1)
- [15th Lok Sabha](json/Lok%20Sabha/15th.json?raw=1)

**Note:**
- The legislative activity of a representative who is a "Minister" is not reported by PRS India. These representatives will have their activity reported as 0 in this dataset.
- Details about a few representatives are unavailable on PRS India. These representatives will be missing in this dataset.

### Minified

Minified datasets, containing a subset of the data available in the above JSONs, can be found as CSV files under the [csv/](csv) folder.

Browse the minified datasets:
- [17th Lok Sabha (Current)](https://flatgithub.com/Vonter/india-representatives-activity?filename=csv/Lok%20Sabha/17th.csv&stickyColumnName=Name)
- [16th Lok Sabha](https://flatgithub.com/Vonter/india-representatives-activity?filename=csv/Lok%20Sabha/16th.csv&stickyColumnName=Name)
- [15th Lok Sabha](https://flatgithub.com/Vonter/india-representatives-activity?filename=csv/Lok%20Sabha/15th.csv&stickyColumnName=Name)
- [Combined (15th-17th) Lok Sabha](https://flatgithub.com/Vonter/india-representatives-activity?filename=csv/Lok%20Sabha.csv&stickyColumnName=Name)

### Aggregated

Aggregated datasets, containing the legislative activity of every representative, grouped by activity type, can be found as CSV files under the [activity/](activity) folder. 

Browse the aggregated datasets:

| Activity | 17th Lok Sabha (Current) | 16th Lok Sabha | 15th Lok Sabha |
|----------------------|---|---|---|
| Debates | [22919 rows](https://flatgithub.com/Vonter/india-representatives-activity?filename=activity/Debates/Lok%20Sabha/17th.csv&stickyColumnName=Debate%20title%2FBill%20name&sort=Date%2Cdesc) | [32713 rows](https://flatgithub.com/Vonter/india-representatives-activity?filename=activity/Debates/Lok%20Sabha/16th.csv&stickyColumnName=Debate%20title%2FBill%20name&sort=Date%2Cdesc) | [18286 rows](https://flatgithub.com/Vonter/india-representatives-activity?filename=activity/Debates/Lok%20Sabha/15th.csv&stickyColumnName=Debate%20title%2FBill%20name&sort=Date%2Cdesc) |
| Questions | [101999 rows](https://flatgithub.com/Vonter/india-representatives-activity?filename=activity/Questions/Lok%20Sabha/17th.csv&stickyColumnName=Title&sort=Date%2Cdesc) | [142340 rows](https://flatgithub.com/Vonter/india-representatives-activity?filename=activity/Questions/Lok%20Sabha/16th.csv&stickyColumnName=Title&sort=Date%2Cdesc) | [143640 rows](https://flatgithub.com/Vonter/india-representatives-activity?filename=activity/Questions/Lok%20Sabha/15th.csv&stickyColumnName=Title&sort=Date%2Cdesc) |
| Private Member Bills | [729 rows](https://flatgithub.com/Vonter/india-representatives-activity?filename=activity/Private%20Member%20Bills/Lok%20Sabha/17th.csv&stickyColumnName=Bill%20title&sort=Date%20of%20introduction%2Cdesc) | [1116 rows](https://flatgithub.com/Vonter/india-representatives-activity?filename=activity/Private%20Member%20Bills/Lok%20Sabha/16th.csv&stickyColumnName=Bill%20title&sort=Date%20of%20introduction%2Cdesc) | [372 rows](https://flatgithub.com/Vonter/india-representatives-activity?filename=activity/Private%20Member%20Bills/Lok%20Sabha/15th.csv&stickyColumnName=Bill%20title&sort=Date%20of%20introduction%2Cdesc) |

## Scripts

- [fetch.sh](fetch.sh): Fetches the raw HTML pages from [PRS India](https://prsindia.org/)
- [flatten.py](flatten.py): Parses the raw HTML pages, and generates the main JSON dataset
- [minify.py](minify.py): Parses the main JSON dataset, and minifies it into CSV files
- [aggregate.py](aggregate.py): Parses the main JSON dataset, and aggregates legislative activity, by activity type, into CSV files

## License

This india-representatives-activity dataset is made available under the Open Database License: http://opendatacommons.org/licenses/odbl/1.0/. 
Users of this data should attribute PRS India: https://prsindia.org

You are free:

* **To share**: To copy, distribute and use the database.
* **To create**: To produce works from the database.
* **To adapt**: To modify, transform and build upon the database.

As long as you:

* **Attribute**: You must attribute any public use of the database, or works produced from the database, in the manner specified in the ODbL. For any use or redistribution of the database, or works produced from it, you must make clear to others the license of the database and keep intact any notices on the original database.
* **Share-Alike**: If you publicly use any adapted version of this database, or works produced from an adapted database, you must also offer that adapted database under the ODbL.
* **Keep open**: If you redistribute the database, or an adapted version of it, then you may use technological measures that restrict the work (such as DRM) as long as you also redistribute a version without such measures.

## Generating

Ensure you have `bash`, `curl` and `python` installed

```
# Fetch the data
bash fetch.sh

# Generate the JSONs
python flatten.py

# Generate the minified CSVs
python minify.py

# Generate the aggregated CSVs
python aggregate.py
```

The fetch script sources data from PRS India (https://prsindia.org/)

## TODO

- State Legislatures
- Rajya Sabha

## Credits

- [PRS India](https://prsindia.org/)

## Related

- [india-election-affidavits](https://github.com/Vonter/india-election-affidavits)
