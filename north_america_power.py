import snap  #Stanford Network Analysis Project 
import csv

UGraph = snap.LoadEdgeList(snap.PUNGraph, "north_america_power.txt", 0, 1)  #load graph from GraphKit NA Power Grid data

#PageRank

PRankH = snap.TIntFltH()   
snap.GetPageRank(UGraph, PRankH)
with open('na_power_pageranks.csv', 'w') as csvfile:  #print pageranks to CSV
    fieldnames = ['node_id', 'page_rank']
    page_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    page_writer.writeheader()

    for item in PRankH:
        page_writer.writerow({'node_id': item, 'page_rank': PRankH[item]})

#Eigenvector Centrality
#epsilon = 10^-4, max_iters = 100
NIdEigenH = snap.TIntFltH()
snap.GetEigenVectorCentr(UGraph, NIdEigenH)
with open('na_power_eigcentr.csv', 'w') as csvfile:  #print eig centralities to CSV
    fieldnames = ['node_id', 'eig_centr']
    eig_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    eig_writer.writeheader()

    
    for item in NIdEigenH:
        eig_writer.writerow({'node_id': item, 'eig_centr': NIdEigenH[item]})

    

#Degree Centrality
#for some reason I get an error when I try to print all three in a single execution of the code;
        #works if you comment one block out
with open('na_power_degcentr.csv', 'w') as csvfile:  #print degree centralities
    fieldnames = ['node_id', 'deg_centr']               
    deg_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    deg_writer.writeheader()

    for NI in UGraph.Nodes():
        n_id = NI.GetId()
        DegCentr = snap.GetDegreeCentr(UGraph, n_id)
        deg_writer.writerow({'node_id': n_id, 'deg_centr': DegCentr})
        
    
