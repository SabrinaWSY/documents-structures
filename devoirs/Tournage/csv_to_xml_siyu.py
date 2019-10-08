# Devoir Cours3 Documents Structurés Siyu WANG
# script pour convertir le ficher csv en xml 
# -*- coding: utf-8 -*-
import csv

def extract_from_file(file_path, sep=';'):
    """
    Extract data from csv file
    :param file_path: the csv file path
    :param sep: the separator string (default to ';')
    :return : titre, realisateur, adresse, organisme, type_tournage, arrondissement, date_debut, date_fin, xy
    """
    titre = []
    realisateur = []
    adresse = []
    organisme = []
    type_tournage = []
    arrondissement = []
    date_debut = []
    date_fin = []
    xy = []

    with open(file_path) as f_tournage:
        tournage_reader = csv.reader(f_tournage, delimiter=sep)
        for row in tournage_reader:
            titre.append(row[0])
            realisateur.append(row[1])
            adresse.append(row[2])
            organisme.append(row[3])
            type_tournage.append(row[4])
            arrondissement.append(row[5])
            date_debut.append(row[6])
            date_fin.append(row[7])
            xy.append(row[8])
            
    return titre, realisateur, adresse, organisme, type_tournage, arrondissement, date_debut, date_fin, xy  

def write_output_file(titre, realisateur, adresse, organisme, type_tournage, arrondissement, date_debut, date_fin, xy, file):
    """ write an output file in xml format """
    with open(file,'w',encoding='utf-8') as xmlfile:
        xmlfile.write("<Lieu_tournage_paris_2011>\n")
        i = 1
        while (i < len(titre)):
            xmlfile.write(f"<titre>{titre[i]}</titre><réalisateur>{realisateur[i]}</réalisateur><adresse>{adresse[i]}</adresse><organisme>{organisme[i]}</organisme><type_tournage>{type_tournage[i]}</type_tournage><arrondissement>{arrondissement[i]}</arrondissement><date_debut>{date_debut[i]}</date_debut><date_fin>{date_fin[i]}</date_fin><xy>{xy[i]}</xy>\n")
            i += 1
        xmlfile.write("</Lieu_tournage_paris_2011>")

titre, realisateur, adresse, organisme, type_tournage, arrondissement, date_debut, date_fin, xy = extract_from_file('./tournagesdefilmsparis2011.csv')
print ("output file generated")
write_output_file(titre, realisateur, adresse, organisme, type_tournage, arrondissement, date_debut, date_fin, xy, "Tournage_output.xml")