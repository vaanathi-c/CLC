Status Report: CLC

For our project, focusing on the Primary Road Density Across ZCTAs: Single- vs Multi-County, this is a recap of our research questions:

- Primary: How does primary road density differ across ZIP Code Tabulation Areas (ZCTAs), and does that pattern change depending on whether a ZCTA lies within one county or crosses county lines?
- Secondary: Which counties and ZCTAs have the highest and lowest primary road density (road km per km² of land)?

We have progressed steadily on our tasks and have accomplished our plan from Week 8 to Week 12, despite facing challenges along the way. Halfway through Week 11, we suddenly found that our originally chosen datasets had suddenly been removed from data.gov. Our progress for the project until then was all lost, so we had to regroup and find new data that we were going to work with. Luckily, we found datasets for the same information, only for different years that we could still analyze. We decided to work with data from 2024 for all three datasets. 

These are our new datasets: 

- TIGER/Line Shapefile, 2024, Nation, U.S., 2020 Census 5-Digit ZIP Code Tabulation Area (ZCTA5)
- TIGER/Line Shapefile, 2024, Nation, U.S., Primary Roads
- TIGER/Line Shapefile, 2024, Nation, U.S., County And Equivalent Entities

We worked in a joint Google Colaboratory notebook throughout the project so that we could collaborate, share code, and help each other out. It has been committed as a copy to our repo in a notebook called Road Density Analysis.ipynb.

This was our previous timeline as established in our project plan: 

- Week 8: Confirm the research question, create a project folder and documentation log (All members)
- Week 9: Download the datasets, review attributes, coordinate systems, and file sizes, and note the different data years (Vaanathi)
- Week 10: Fix invalid geometries, decide how to filter U.S. territories (e.g., Alaska) (Lana)
- Week 11: Perform intersection between ZCTA boundaries and county polygons to categorize ZCTAs into single county or multi-county (Joanne)
- Week 12: Conduct summary statistics and fit a simple regression model and break down results by state and region (Bharathi)
- Week 13: Build maps of road density and charts comparing single vs. multi-county ZCTAs (Vaanathi & Lana)
- Week 14: Draft the report covering the methods, results, limitations, and possible extensions (Joanne & Bharathi)
- Week 15: Proofread, make sure results are reproducible, and submit final report (All Members)

We have completed all of our planned tasks from Week 8 - Week 12, so we are on track to finish our project as planned. Our timeline does not require any updates. We also overcame some of the constraints listed in our project plan by standardizing the year across all of our chosen datasets to 2024. 

Contribution by member: 

Vaanathi: I downloaded all three datasets to inspect them, then I looked at all the attributes in each dataset (ZCTA5CE20, GEOID20, LINEARID, FULLNAME, STATEFP, COUNTYFP, etc.). After that, I checked the coordinate reference system for each file and made sure they matched, since we need consistent projections before doing any spatial work. I also recorded the file sizes and noted the data years, which became important when our original datasets were removed from data.gov. Once that happened, I helped confirm that the 2024 TIGER/Line versions had the same attributes and structure as the originals, so we could standardize all three datasets to one year and keep going. I also drafted the initial structure of the project plan, and the rest of the team made changes as they saw fit.

Lana: I handled data cleaning for our three datasets. I ran validity checks on the geometries in each file and repaired the invalid ones so they wouldn’t cause errors in later spatial operations. I also worked out how to handle U.S. territories and non-contiguous areas like Alaska, since they can distort density calculations and make maps hard to read. I documented the filtering decisions and the reasoning behind them so the team can reproduce the same steps and explain our choices in the final report. 

Bharathi: I worked on the analysis phase. Using the processed data, I calculated summary statistics for primary road density (road km per km² of land) across ZCTAs, including the means, medians, and spread, and identified which counties and ZCTAs had the highest and lowest density. I then fit a simple regression model to test whether density differs between single-county and multi-county ZCTAs, and broke the results down by state and region to see whether the pattern holds across different parts of the country. 

Joanne: I performed the spatial intersection between the ZCTA boundaries and the county polygons. For each ZCTA, I determined how many counties it overlaps and used that to classify it as single-county or multi-county. This classification is the core variable for our primary research question, so I checked the results carefully, including handling tiny boundary overlaps that could cause a ZCTA to be mislabeled as multi-county. I finished this step after we replaced our datasets, so I redid the intersection with the 2024 files and saved the output for the rest of the team to use. 
