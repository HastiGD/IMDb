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
      "       tconst parentTconst  seasonNumber  episodeNumber\n",
      "0   tt0041951    tt0041038           1.0            9.0\n",
      "1   tt0042816    tt0989125           1.0           17.0\n",
      "2   tt0042889    tt0989125           NaN            NaN\n",
      "3   tt0043426    tt0040051           3.0           42.0\n",
      "4   tt0043631    tt0989125           2.0           16.0\n",
      "5   tt0043693    tt0989125           2.0            8.0\n",
      "6   tt0043710    tt0989125           3.0            3.0\n",
      "7   tt0044093    tt0959862           1.0            6.0\n",
      "8   tt0044668    tt0044243           2.0           16.0\n",
      "9   tt0044901    tt0989125           3.0           46.0\n",
      "10  tt0045519    tt0989125           4.0           11.0\n",
      "11  tt0045960    tt0044284           2.0            3.0\n",
      "12  tt0046135    tt0989125           4.0            5.0\n",
      "13  tt0046150    tt0341798           NaN            NaN\n",
      "14  tt0046855    tt0046643           1.0            4.0\n",
      "15  tt0046864    tt0989125           5.0           20.0\n",
      "16  tt0047810    tt0914702           3.0           36.0\n",
      "17  tt0047852    tt0047745           1.0           15.0\n",
      "18  tt0047858    tt0046637           2.0            9.0\n",
      "19  tt0047961    tt0989125           6.0            5.0\n"
     ]
    }
   ],
   "source": [
    "import pandas\n",
    "\n",
    "### Title Episode Table\n",
    "\n",
    "# load the episode dataset into a df\n",
    "path = \"/Users/hastigheibidehnashi/DBMS/IMDb/raw_data/\"\n",
    "file = \"title.episode.tsv.gz\"\n",
    "episode_df = pandas.read_csv(path+file, sep=\"\\t\", na_values=\"\\\\N\", nrows = 20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       tconst parentTconst  seasonNumber  episodeNumber\n",
      "0   tt0041951    tt0041038             1              9\n",
      "1   tt0042816    tt0989125             1             17\n",
      "2   tt0042889    tt0989125          <NA>           <NA>\n",
      "3   tt0043426    tt0040051             3             42\n",
      "4   tt0043631    tt0989125             2             16\n",
      "5   tt0043693    tt0989125             2              8\n",
      "6   tt0043710    tt0989125             3              3\n",
      "7   tt0044093    tt0959862             1              6\n",
      "8   tt0044668    tt0044243             2             16\n",
      "9   tt0044901    tt0989125             3             46\n",
      "10  tt0045519    tt0989125             4             11\n",
      "11  tt0045960    tt0044284             2              3\n",
      "12  tt0046135    tt0989125             4              5\n",
      "13  tt0046150    tt0341798          <NA>           <NA>\n",
      "14  tt0046855    tt0046643             1              4\n",
      "15  tt0046864    tt0989125             5             20\n",
      "16  tt0047810    tt0914702             3             36\n",
      "17  tt0047852    tt0047745             1             15\n",
      "18  tt0047858    tt0046637             2              9\n",
      "19  tt0047961    tt0989125             6              5\n"
     ]
    }
   ],
   "source": [
    "# convert seasonNumber and episodeNumber to int\n",
    "episode_df[\"seasonNumber\"] = episode_df[\"seasonNumber\"].astype('Int64')\n",
    "episode_df[\"episodeNumber\"] = episode_df[\"episodeNumber\"].astype('Int64')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# save formatted data as new tsv file\n",
    "path = \"/Users/hastigheibidehnashi/DBMS/IMDb/IMDb_Database/data/\"\n",
    "file = \"episode.tsv\"\n",
    "episode_df.to_csv(path+file, sep=\"\\t\")"
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
