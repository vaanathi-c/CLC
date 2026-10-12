**Overview**: Our team will be looking through the three datasets (zip code, roads, and county) underneath. The goal of this project is to examine how primary road density varies across ZIP Code Tabulation Areas (ZCTAs) in the United States, and whether that pattern differs for ZCTAs that fall entirely within one county versus those that cross county lines. Due to the fact that ZIP-level and county-level data are often joined in practice, we want to understand how these two boundary systems relate and whether the mismatch between them is associated with differences in highway access. The central question is: How does primary road density differ across ZIP Code Tabulation Areas, and does that pattern change depending on whether a ZCTA lies within one county or crosses county lines?
Our project will focus on data acquisition, quality assessment, cleaning, integration, and analysis. First, we will download three TIGER/Line shapefiles containing ZCTA boundaries, primary road networks, and county boundaries. We will assess data quality by identifying missing geographic information, duplicate records, inconsistent coordinate reference systems, and potential boundary discrepancies. Based on these findings, we will clean and standardize the datasets to ensure compatibility.
Next, we will integrate the datasets by geographic intersections, and then we will focus on our main research question for the remainder of our analysis.

**Team & Roles:**
Each team member will be analyzing all three datasets so that we can all share our opinions on the datasets. More specifically, each member of the team will be doing the following:
Bharathi: Data Acquisition – Download datasets, review metadata, and document data sources and formats.
Joanne: Data Quality Assessment – Identify missing values, duplicates, inconsistent geographic information, and other quality issues.
Lana: Data Cleaning and Integration –  Standardize datasets, resolve identified quality issues, and implement spatial joins.
Vaanathi: Analysis and Documentation –  Calculate road coverage metrics, create visualizations, and compile the final project documentation.


**Research Questions:**

Primary Research Question: How does primary road density differ across ZIP Code Tabulation Areas, and does that pattern change depending on whether a ZCTA lies within one county or crosses county lines?

Secondary Research Question: Which counties and ZCTAs have the highest and lowest primary road density, measured as road length per unit of geographic area?


**Datasets:**
We chose the following three datasets for our research project: (1) ZIP Code Tabulation Areas (ZCTAs), (2) Primary Roads, (3) Counties. 

https://catalog.data.gov/?sort=popularity&q=&sort=popularity&spatial_filter=&org_slug=census (website link)

TIGER/Line Shapefile, 2022, Nation, U.S., 2020 Census 5-Digit ZIP Code Tabulation Area (ZCTA5) 

TIGER/Line Shapefile, 2023, Nation, U.S., Primary Roads 

TIGER/Line Shapefile, Current, Nation, U.S., County and Equivalent Entities 


Timeline: The detailed plan is the following (the “week” are the due dates, the tasks are presented along with the people responsible for completing the tasks.
Week 8: Confirm the research question, create a project folder and documentation log (All members)
Week 9: Download the datasets, review attributes, coordinate systems, and file sizes, and note the different data years (Vaanathi)
Week 10: Fix invalid geometries, decide how to filter U.S. territories (e.g., Alaska) (Lana)
Week 11: Perform intersection between ZCTA boundaries and county polygons to categorize ZCTAs into single county or multi-county (Joanne)
Week 12: Conduct summary statistics and fit a simple regression model and break down results by state and region (Bharathi)
Week 13: Build maps of road density and charts comparing single vs. multi-county ZCTAs (Vaanathi & Lana)
Week 14: Draft the report covering the methods, results, limitations, and possible extensions (Joanne & Bharathi)
Week 15: Proofread, make sure results are reproducible, and submit final report (All Members)

**Constraints:**
Differences in dataset years: The ZCTA dataset is based on 2020 Census geography and was published as a 2022 shapefile, while the road dataset is from 2023 and the county dataset is labeled current. Geographic boundaries may differ between releases, which requires standardization.
Data volume and processing complexity: Nationwide geographic datasets may require significant processing time and memory. We may limit the geographic scope or process the data in smaller geographic subsets if necessary.
Data quality: Missing attributes, duplicate features, invalid geometries, and inconsistent coordinate reference systems may complicate integration. We will document identified issues, apply appropriate cleaning methods, and validate the resulting datasets.

**Gaps:**
Data mismatch: We identified that the ZCTAs dataset is from 2022, the Primary Roads dataset is from 2023, and the County dataset is the “current” release all have varying time frames. We need to decide how to fix our dataset time frame to a specific year to all match one year. Input needed: whether a 1 or 2 year mismatch is acceptable for the project.
 Definition of Primary Roads: The Primary Roads dataset covers only major limited-access highways, predominantly interstates, and happens to leave out most U.S. and state highways and all local roads. A ZCTA with zero primary-road density may still have good road access, so the results reflect highway access only. Input needed: a decision on whether to document this as a limitation or add the Primary and Secondary dataset for a broader picture.
Geographic Scope: We have not yet decided how to handle Alaska, Hawaii, Puerto Rico and other territories. Each needs a different projection for accurate measurement, and their road networks differ greatly from the mainland U.S. Input needed: whether to limit the analysis to the contiguous 48 states or include or all areas.

