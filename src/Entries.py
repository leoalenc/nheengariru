#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leonel Figueiredo de Alencar
# Last update: September 2, 2023

from Nheengariru import *

example1=Example("Kunhã usika ramé, usasá amú suaxara rupí, unheẽ: ― Taité! Umanú ana.",Source("Magalhães", 255),"Quando a mulher chegou, passou pelo outro lado e disse: ― Coitada! Já morreu.")
example2=Example("Teité araã Supy, teité araã yandé!",Source("Amorim", 124),"Coitado de Supy, coitadas de nós!")
example3=Example("Nuká paá taité urikú sapekwerantu piranga i ayura upé, aité paá tatá kwera nhaã.",Source("Leetra Indígena. n. 17", 73), "No entanto, dizem que o pobre tinha só a marca vermelha em seu pescoço, dizem que aquilo foi o fogo.")
example4=Example("Nhaã Tuyuka Manha pirera kwera uyuíri uyari yané resé. Yawé arã paá yandé, taité, ti yasemu purapuranga.", Source("Leetra Indígena. n. 17", 37), "A máscara da Mãe do Barro voltou e aderiu em nós. Por isso, nós, coitados, não saímos muito bonitos.")
	
	
def ExampleEntry():
	lemma=Lemma("teité")
	taite = Variant("taité")
	tete = Variant("teté", True)
	# TODO: formlist is actually more complicated to obtain because of inflection (relational prefixes, conjugation, etc.) and derivation
	formlist=['teité','taité','teté']
	sense_example1=SenseExample(example1,formlist)
	sense_example2=SenseExample(example2,formlist)
	sense1=Sense(INTERJ,"(exprime compadecimento:) coitado (a, os, as)!, pobrezinho (a, os, as)!, TEITÉ! (PA)",1,[],[sense_example1,sense_example2])
	sense_example3=SenseExample(example3,formlist)
	sense_example4=SenseExample(example4,formlist)
	sense2=Sense(NOUN_ADJ,"coitado (de), coitadinho (de), pobre, miserável",2,[],[sense_example3,sense_example4])
	formlist1=FormList(['teté', 'tete', 'tetê'],[177, 188, 194, 243])
	formlist2=FormList(['taité'], [243, 255])
	histreg1=HistoricalRegister('Magalhães',[formlist1,formlist2])
	et=Etymology('tupi',"teté")
	return Entry(lemma,None,[taite,tete],[sense1,sense2],[histreg1],et)

def ExampleEntry2():
	ete = Variant("ité",True)
	amorim=Source("Amorim",179)
	baena=Source("Baena",110)
	# TODO: include anchors of the examples
	# TODO: Objects of the Example class should be defined outside individual entries since individual examples are often used in different entries throughtout the dictionary
	example1=Example("Mairamé mira urikú waá wirá akanga umaã teyú usasá suakí, uyeréu mira eté, umuatá mirapara, [...].", amorim, "Quando a pessoa que tinha cabeça de pássaro viu o lagarto passar perto dela, virou gente de verdade, entesou o arco, [...].")
	example2=Example("Itakamutí pupé ne yasukawa, pitangé puranga ité.", baena, "Numa pia de pedra foi o teu batismo, ó menino muito bom.")
	sourcelist1=SourceList([])
	sourcelist1.fromstring("Tastevin, 620; Amorim, 179; Stradelli, 364")
	#sourcelist1=mkSourceList("Tastevin, 620; Amorim, 179; Stradelli, 364")
	equivalent=Equivalent("reté",1,1)
	sense1=Sense(ADJ,"real, verdadeiro, legítimo, de verdade",1,[],[example1],sourcelist=sourcelist1, usage_note='''atualmente ainda ocorre em alguns compostos''',equivalent=equivalent)
	sourcelist2=SourceList([])
	sourcelist2.fromstring("Tastevin, 620")
	sense2=Sense(ADJ,"respeitável, digno",2,[],[],sourcelist=sourcelist2)
	sourcelist3=SourceList([])
	sense3=Sense(ADV,"muito",3,[],[example2],sourcelist3.fromstring("Coudreau, 466; Studart, 28; Stradelli, 364; Baena, 110"),equivalent=Equivalent("reté",1,4))
	formlist1=FormList(['ete', 'ite'],[620])
	formlist2=FormList(['eté'], [179])
	histreg1=HistoricalRegister('Tastevin',[formlist1])
	histreg2=HistoricalRegister('Amorim',[formlist2])
	et=Etymology('tupi',"eté (r, s)")
	lemma=Lemma("eté", True)
	return Entry(lemma,None,[ete],[sense1,sense2,sense3],[histreg1],et)

