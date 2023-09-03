#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Leonel Figueiredo de Alencar
# Last update: September 2, 2023


class Category:
	"""A class to represent the categorization of a lemma.
		
		Args:
			lexcat (list): List of lexical categories.
			subcat (list): List of subategorization labels, e.g., ['tr','intr'].
			semantic_domain (str): Semantic domain label, e.g., 'astron'.
			
		"""
	def __init__(self,lexcat,subcat=[],semantic_domain=[]):
		self.lexcat = lexcat
		self.subcat = subcat
		self.semantic_domain = semantic_domain
		
class LexicalCategory:
	"""A class to represent the lexical category of a lemma.
		
		Args:
			label (str): Lexical category label, e.g., 's', 'adj', etc.
			
		"""
	# TODO: Substitute v2 and v3 for Avila's 'v. 2ª cl.', 'v. 3ª cl.' labels.
	def __init__(self,label):
		self.label = label
		
	def tycho(self):
		"""Return the corresponding tag in the Tycho Brahe Corpus Annotation System.
		"""
		mapping={'s':'N',
		   'v': 'VB', # etc.
			   } 
		return mapping.get(self.label,self.label.upper())
	
	def upos(self):
		"""Return the corresponding tag in the Universal Dependencies Annotation System.
		"""
		mapping={'s':'NOUN',
		   'v': 'VERB', # etc.
			   } 
		return mapping.get(self.label)
	# implement a sinle method based on an n+1 column table for n annotation systems
	
	def inflection(self):
		"""Return inflectional class encoded in Avila's lexical category label, e.g., 'v. 2ª cl.', 'v. 3ª cl.', etc.
		"""
		pass

class Subcat:
	"""A class to represent subcategorization (valence).
		
		Args:
			label (str): Avila's valence class, e.g., 'tr', 'intr', etc.
			hist (bool): Whether the valence is historical.
			obso (bool): Whether the valence is obsolete.
		"""
	def __init__(self,label,hist=False,obso=False):
		self.label = label
		self.hist = hist
		self.obso = obso

# TODO: merge with Usage class.		
class SemanticDomain:
	"""A class to represent the semantic domain (Avila, 2021, p. 152).
		
		Args:
			label (str): Semantic domain label.
			
		"""
	def __init__(self,label):
		self.label = label
		
	def translate(self):
		translation={'ethno' : 'etnôm', 'topo': 'topôn'}
		return translation.get(self.label,self.label)
		
class Ethnonym(SemanticDomain):
	"""A class to represent ethnonyms.
		
		"""
	def __init__(self):
		super().__init__('ethnon')
		
class Toponym(SemanticDomain):
	"""A class to represent toponyms.
		
		"""
	def __init__(self):
		super().__init__('topon')

class Astronomical(SemanticDomain):
	"""A class to represent astronomical terms.
		
		"""
	def __init__(self):
		super().__init__('astron')

"""11. Style
This concerns style, register, connotations and any kind of pragmatic information. The same restrictions as in the previous fields apply. Relevant values include ‘ritual’, ‘formal’, ‘vulgar’. Cf. Wahrig 1973, ch. 4.
https://www.christianlehmann.eu/ling/ling_meth/ling_description/lexicography/index.html?https://www.christianlehmann.eu/ling/ling_meth/ling_description/lexicography/microstructure.html
"""

"""Information items concerning the proper use and usage restrictions of a lexical item ('Pragmatische Angaben' (PragA)): relating to the subject ('Fachgebietsangabe' (FGA)), the stylistic level ('Stilschichtenangaben' (StilA)), the frequency of use ('Häufigkeitsangabe' (HA)), the diachronic level ('diachrA)), geographic restriction of usage, etc. They are typically subsumed under the meaning section.
Other: etymology ('Etymologische Angabe' (EtyA)), cross-references ('Verweisangabe' (VerwA)).
http://milca.sfs.uni-tuebingen.de/B2/Textbook/DictStruct/MiLCA_COLEX_DictStruct-03.xhtml#:~:text=The%20term%20microstructure%20denotes%20the,entries%20of%20a%20particular%20dictionary.
"""
class Usage:
	"""A class to represent usage.
		
		"""
	def __init__(self,label):
		self.label = label
		
	def translate(self):
		translation={'bib' : 'bíb'}
		return translation.get(self.label,self.label)

class HistoricalUsage(Usage):
	def __init__(self,adapt=False):
		super().__init__('hist')
		self.adapt=adapt

class BiblicalUsage(Usage):
	def __init__(self):
		super().__init__('bib')
		
# TODO: use the following three classes in the three classes above?
class Label:
	def __init__(self,label):
		self.label=label
		self.boolean=True

class Historical(Label):
	def __init__(self,adapt=False):
		super().__init__('hist')
		self.adapt=adapt

class Biblical(Label):
	def __init__(self):
		super().__init__('bib')
		
class Lemma:
	def __init__(self,form,num=0,hist=False,adapt=False,obso=False):
		"""A class to represent a lemma.
		
		Args:
			form (str): Orthographic form of the lemma.
			num (int): Superscript index distinguishing homonyms.
			hist (bool): Whether the lemma is historical.
			adapt (bool): Whether the lemma is adapted.
			obso (bool): Whether the lemma is obsolete.
			
		"""
		self.form = form #TODO: 'ortho' instead of 'form'
		self.num = num
		self.hist = hist 
		self.adapt = adapt
		self.obso = obso
		# TODO: Employ parameter 'usage' with the the values 'hist', 'obso', 'hist. adapt.' and 'bib(lical)' See Avila 2021, p. 153-158.
		
	def label(self): # TODO: implement label and num as classes
		adapt=''
		label=''
		if self.hist:
			if self.adapt:
				adapt=' adapt.'
			label=f"[hist.{adapt}]"
		elif self.obso:
			label=f"[obso.]"
		return label
	
	def index(self):
		if self.num:
			return f"<sup>{self.num}</sup>"
		else:
			return ''
	
	def __str__(self):
		return f"{self.form}{self.index()} {self.label()}"
	
class RelPrefLemma(Lemma):
	"""A class to represent a lemma with relational prefixes.
	
	"""
	def __init__(self,form,num=0,hist=False,adapt=False,obso=False,relprefs={}):
		"""
		Args:
			relprefs (RelationalPrefixes): Relational prefixes.
		"""
		super().__init__(form,num,hist,adapt,obso)
		self.relprefs=relprefs
		#TODO: provide alternative constructor accepting dictionary
	
	def __str__(self):
		parts=[f"{self.form}{super().index()}"]
		parts.append(f"({self.relprefs.__str__()})")
		label=super().label()
		if label:
			parts.append(label)
		return f"{' '.join(parts)}"
	
class Variant(Lemma):
	"""A class to represent a lemma variant.
	
	"""

class RelPrefVariant(RelPrefLemma):
	"""A class to represent a lemma variant with relational prefixes.
	
	"""
class Equivalent:
	"""A class to represent a synonymous lemma.
	
	Args:
		lemma (str): Orthographic form of a lemma.
		num (int): Superscript index of lemma.
		sensenum (int): Numerical index of the lemma sense.
		
	"""
	def __init__(self,lemma,num=0,sensenum=0):
		self.lemma = lemma
		self.num = num
		self.sensenum = sensenum

class Source:
	"""A class to represent a bibliographical source.
	
	Args:
		author (str): Author's last name.
		page (int): Page number.
		
	"""
	def __init__(self,author,page):
		self.author = author
		self.page = page
		
class SourceList:
	"""A class to represent a list of bibliographical sources (Avila 2021:164-165).
	
	Args:
		sourcelist (list): List of bibliographical sources.
		
	"""
	def __init__(self,sourcelist):
		self.sourcelist = sourcelist
	
	def fromstring(self,sources):
		for source in sources.split(";"):
			author,page=source.split(",")
			page=int(page.strip())
			self.sourcelist.append(Source(author,page))

# TODO: cat (Category) (see above) instead of pos (str)

class Sense:
	"""A class to represent a sense of a lemma.
	
	Args:
		cat (Category): Categorial information.
		definition (str): Sense definition.
		num (int): Sequence number of the sense.
		examples (list): List of SenseExamples instances.
		usage (Usage): Sense usage. 
		sourcelist (Sourcelist): List of bibliographical sources.
		usage_note (str): Explanation about the use of the sense.
		equivalent (Equivalent): Synonymous lemma.
		
	"""
	def __init__(self,cat,definition,num=None,subsenses=[],examples=[],usage=None,sourcelist=[],usage_note='',equivalent=None):
		self.cat = cat
		self.definition = definition
		self.num = num
		self.subsenses = subsenses
		self.examples = examples
		self.usage = usage
		self.sourcelist = sourcelist
		self.usage_note = usage_note
		self.equivalent = equivalent

class Subsense(Sense):
	"""A class to represent a subsense of a sense.
	
	"""
	def index(self):
		from string import ascii_lowercase as letters
		return letters[self.num-1]
	
class Example:
	def __init__(self,yrl,source,por,adapt=True):
		self.yrl = yrl
		self.source = source
		self.por = por
		self.adapt = adapt
		
	def __str__(self):
		source=''
		if not self.source:
			source=f" ({self.source})"
		return f"{self.yrl}{source} - {self.por}"

class SenseExample:
	"""A class to represent an example of the usage of a sense.
	
	Args:
		example (Example): An instance of the Example class.
		formlist (list): List of forms. 
	
	"""
	def __init__(self, example,formlist):
		self.example = example
		#self.anchorspans = anchorspans
		self.anchorspans = None
		self.fromformlist(formlist)
	# TODO: Is there a better way to do this?
	
	def findall(self,substring):
		"""Return start and end indexes of all occurrences of substring in string.
		
		"""
		string=self.example.yrl.lower()
		substring=substring.lower()
		span=len(substring)
		length=len(string)-span
		i=0
		indexes=[]
		while(i<=length):
			start=i
			end=i+span
			if string[start:end]==substring:
				indexes.append((start,end))
				i=end
			i+=1
		return indexes
	
	def spans(self,indexes):
		"""Return a list of AnchorSpan instances for each (start,end) tuple from a list.
		
		Args:
			indexes (list): List of (start,end) tuples, where start and end are positive integers.
		
		"""
		self.anchorspans=[AnchorSpan(start, end) for start,end in indexes]
		
	def fromformlist(self,formlist):
		indexes=[]
		for form in formlist:
			indexes.extend(self.findall(form))
		self.spans(indexes)

class AnchorSpan:
	"""A class to represent an occurrence of a word in an example.
	
	Args:
		start (int): The start index in the example string.
		end (end): The end index in the example string.
	
	"""
	def __init__(self, start,end):
		self.start = start
		self.end = end
	
# TODO: use 'ortho' instead of 'form' (likewise 'phon' if phonemic representation is adopted)
class RelationalPrefix():
	def __init__(self,form,hypoth=False,hist=False):
		self.form = form
		self.hypoth = hypoth
		self.hist = hist
	
class AbsolutivePrefix(RelationalPrefix):
	num=4
	name='absolutive'
	abbrev='ABS' # Lehmann (2004, p. 15)

class ContiguityPrefix(RelationalPrefix):
	num=1
	name='contiguity'
	abbrev='CONT'
	def __init__(self,hypoth=False,hist=False):
		super().__init__('r',hypoth,hist)

class NonContiguityPrefix(RelationalPrefix):
	num=2
	name='non-contiguity'
	abbrev='NCONT'
	alternating=False
	
	def alternant(self,theme):
		"""
		Args:
			theme (str): orthographical form of the lemma's theme
		"""
		return None

class AlternatingNContPref(NonContiguityPrefix):
	alternating=True
	def __init__(self,hypoth=False,hist=False):
		super().__init__('s',hypoth,hist)
		
	def alternant(self,theme):
		"""phonetic realization rule /s/ -> [ʃ] _/i/  (see Cruz 2011, p. 137 for a similar approach)"""
		form=self.form
		if theme.startswith("i"):
			form='x'
		return f"{form}"

class PostalveolarFricativeNContPref(NonContiguityPrefix):
	def __init__(self,hypoth=False,hist=False):
		super().__init__('x',hypoth,hist)
		
class AlveolarFricativeNContPref(NonContiguityPrefix):
	def __init__(self,hypoth=False,hist=False):
		super().__init__('s',hypoth,hist)

class PlosiveNContPref(NonContiguityPrefix):
	def __init__(self,hypoth=False,hist=False):
		super().__init__('t',hypoth,hist)
		
class RelationalPrefixes:
	def __init__(self,absol=None,cont=None,ncont=None):
		self.absol = absol
		self.cont = cont
		self.ncont = ncont
	
	def dictionary(self):
		dic={}
		dic['abs']=self.absol
		dic['cont']=self.cont
		dic['ncont']=self.ncont
		return dic
	
	def __str__(self):
		dic=self.dictionary()
		prefixes=[]
		for k,v in dic.items():
			if v:
				form=v.form
				if v.hypoth:
					leftb="["
					rightb="]"
				elif v.hist:
					leftb="{"
					rightb="}"
				else:
					leftb=''
					rightb=''
				if v.num == 2 and v.alternating:
					form='s/x'
				form=f"{leftb}{form}{rightb}"
				prefixes.append(form)
		return f"{', '.join(prefixes)}"

"""
three certainty levels:

Thompson et al. (2011) apply five meta-knowledge features - manner, source, polarity, certainty, and knowledge type - to the GENIA event corpus (GENIA Event Extraction , GENIA). This corpus is composed of Medline abstracts split into individual statements. With respect to certainty annotations, the corpus utilizes a classification system of three certainty levels - certain, probable (some degree of speculation), and doubtful (currently under investigation). Annotation was carried out by two linguistic specialists specifically trained in the meta-knowledge scheme.

Prieto M, Deus H, de Waard A, Schultes E, García-Jiménez B, Wilkinson MD. Data-driven classification of the certainty of scholarly assertions. PeerJ. 2020 Apr 21;8:e8871. doi: 10.7717/peerj.8871. PMID: 32341891; PMCID: PMC7182025.
"""

class Etymology:
	"""A class to represent etimological information about a lemma.
	
	Args:
		origlang (str): Language of origin.
		orig (str): Etymon.
		gloss (str): Glossing of the meaning of the etymon.
		certainty (bool): Whether the etymology is certain. # TODO: use modal adverb as parameter
	"""
	
# TODO: provide alternative constructor with the modal adverbs used by Avila (2021)
	def __init__(self,origlang,orig,gloss='',certainty=True):
		self.origlang = origlang
		self.orig = orig
		self.gloss = gloss
		self.certainty = certainty
		# TODO: include additional attributes (morphemic analysis etc.)
	def __str__(self):
		modal=''
		if not self.certainty:
			modal='talvez ' # TODO: include "provavelmente"
		return f"{modal}do {self.origlang} {self.orig}"

class FormList:
	def __init__(self,forms,pages):
		self.forms = forms
		self.pages = pages
		
class HistoricalRegister:
	"""A class to represent a historical register.
	
	"""
	def __init__(self,source,formlists):
		self.source = source
		self.formlists = formlists
		
		
class Entry:
	"""A class to represent a dictionary entry.
	
	Args:
		lemma (Lemma): The main headword of the entry .
		cat (Category): Categorial information.
		variants (list): List of lemma variants.
		senses (list): List of senses.
		histreglist (list): List of historical registers.
		etim (Etimology): Etimological information about the lemma. 
		
	"""
	def __init__(self,lemma,cat,variants,senses,histreglist,etim):
		self.lemma = lemma
		self.cat = cat
		self.variants = variants
		self.senses = senses
		self.histreglist = histreglist
		self.etim = etim
		
	def __str__(self):
		return f"{self.lemma}"
	
def mkSourceList(sources):
	sourcelist=[]
	for source in sources.split(";"):
		author,page=source.split(",")
		page=int(page.strip())
		sourcelist.append(Source(author,page))
	return SourceList(sourcelist)
	

# TODO: Place these objects in a separate module? Implement them as classes?
# TODO: Include all labels from Avila (2021).
NOUN_LEXCAT=LexicalCategory('s')
ADJ_LEXCAT=LexicalCategory('adj')
ADV_LEXCAT=LexicalCategory('adv')
VERB_LEXCAT=LexicalCategory('v')
V2_LEXCAT=LexicalCategory('v2')
V3_LEXCAT=LexicalCategory('v3')
INTERJ=Category([LexicalCategory('interj')])
NOUN=Category([NOUN_LEXCAT])
ADJ=Category([ADJ_LEXCAT])
ADV=Category([ADV_LEXCAT])
VERB=Category([VERB_LEXCAT])
NOUN_ADJ=Category([NOUN_LEXCAT,ADJ_LEXCAT])
V2_ADJ=Category([V2_LEXCAT,ADJ_LEXCAT])


