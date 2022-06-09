# SEARCH ENGINE REQUIREMENTS

**Problem Statement**: The main problem is the effective indexing of web pages and showing them in a
presentable form to the user looking for a specific information. A user will only look at the first 10
results of a search query but how will the search engine determine the reputation and importance of a
web page among a possible million others?

**Domain/Scope:** A Web Page

**Database:**
• Simple Wikipedia database downloaded from:
https://phabricator.wikimedia.org/source/mediawiki/browse/master/maintenance/tables.sql
• Wikipedia has approximately 5 million+ pages.
• These pages consist of information on topics such from historical figures to educational topics
and so forth, Wikipedia is the world’s largest encyclopedia on almost every daily topic in our life.
• We will be creating test cases on 1000 links at first and calculate time our algorithm takes on
single and muti-word queries and extrapolate the time for larger datasets. Then run our tests to
confirm whether the time matches or not. We will also cross reference our search results with
that of Google, using: query site:wikipedia.org.

**Concepts Involved/Functionality:**
• **PageRank** which is essentially determined by factors which will constitute the meta information
such as: reputation of the source, update frequency, quality, popularity or usage, and citations.
• We are using the Wikipedia database since it has a diverse range of information on various
topics. We will be demonstrating our algorithm implementation on a dataset between 50,000
and 100,000 links.
• **Forward Index:** Partially sorted index containing wordIDs.
• **Inverted Index:** Index which has been processed by the sorter.
• Our search engine focuses on 'text' format. A user would be able to search for tables, link lists,
general lists, short pages, long pages, simple pages etc.

**Technologies Required:**
• Python IDE, Visual Studio C++ Integration using Boost Libraries.
• MySQL Database for storing indexes and webpages.
• Xampp/Apache - Lucene for localhost creation and webpage hosting.
• HTML5, CSS and Bootstrap for user interface of the webpage
