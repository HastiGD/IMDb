{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       tconst  averageRating  numVotes\n",
      "0   tt0000001            5.6      1658\n",
      "1   tt0000002            6.1       201\n",
      "2   tt0000003            6.5      1370\n",
      "3   tt0000004            6.2       122\n",
      "4   tt0000005            6.2      2158\n",
      "5   tt0000006            5.3       115\n",
      "6   tt0000007            5.4       661\n",
      "7   tt0000008            5.4      1822\n",
      "8   tt0000009            5.9       155\n",
      "9   tt0000010            6.9      6077\n",
      "10  tt0000011            5.2       266\n",
      "11  tt0000012            7.4     10423\n",
      "12  tt0000013            5.7      1584\n",
      "13  tt0000014            7.1      4654\n",
      "14  tt0000015            6.1       829\n",
      "15  tt0000016            5.9      1210\n",
      "16  tt0000017            4.6       243\n",
      "17  tt0000018            5.3       480\n",
      "18  tt0000019            5.3        20\n",
      "19  tt0000020            5.0       268\n"
     ]
    }
   ],
   "source": [
    "import pandas\n",
    "\n",
    "### Title Rating Table\n",
    "\n",
    "# load the rating dataset into a df\n",
    "path = \"/Users/hastigheibidehnashi/DBMS/IMDb/raw_data/\"\n",
    "file = \"title.ratings.tsv.gz\"\n",
    "rating_df = pandas.read_csv(path+file, sep=\"\\t\", na_values=\"\\\\N\", nrows = 20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# save formatted data as new tsv file\n",
    "path = \"/Users/hastigheibidehnashi/DBMS/IMDb/IMDb_Database/data/\"\n",
    "file = \"rating.tsv\"\n",
    "rating_df.to_csv(path+file, sep=\"\\t\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
