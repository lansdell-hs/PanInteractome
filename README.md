# PanInteractome
Scripts used to help facilitate the construction of a binary protein interaction network 

Fasta Combiner: Takes all .faa files in a directory and creates a new file with the same extension with a separtion line between each file's contents. 

Runner: Calls the subprocess command to act upon all the fasta files in a directory to process the command to run EggNOG's downloadable annotation program. 

EggNOG_scraper: A work in progress program that attempts to submit individual proteins into the query field of http://eggnogdb.embl.de/ and scrape the COG identifier associated with the individual protein.  



CITATION: eggNOG 4.5: a hierarchical orthology framework with improved functional
      annotations for eukaryotic, prokaryotic and viral sequences. Jaime
      Huerta-Cepas, Damian Szklarczyk, Kristoffer Forslund, Helen Cook, Davide
      Heller, Mathias C. Walter, Thomas Rattei, Daniel R. Mende, Shinichi
      Sunagawa, Michael Kuhn, Lars Juhl Jensen, Christian von Mering, and Peer
      Bork. Nucl. Acids Res. (04 January 2016) 44 (D1): D286-D293. [doi:
      10.1093/nar/gkv1248](http://doi.org/10.1093/nar/gkv1248)
