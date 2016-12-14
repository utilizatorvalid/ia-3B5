
# ===================================================================
# = model.py - Core and External Classes of the Music Ontology 
# =            Generated automatically on Thu Sep 20 16:42:02 2007
# ===================================================================


from mopy.PropertySet import PropertySet, protector


def objToStr(c):
	s = "-- "+c.shortname
	if c.URI != None :
		s+=" @ "+str(c.URI)
	s+=" --\n"
	for p in c._props.keys():
		for v in c._props[p]:
			s+=c._props[p].shortname + " : "
			if isinstance(v, c._props[p].Lits):
				s+=str(v)
			else:
				s+=str(type(v))
				if hasattr(v,"URI") and v.URI != None:
					s+=" @ "+v.URI
			s +="\n"
	return s

# ======================== Property Docstrings ====================== 

propDocs = {}
propDocs["hasAgent"]=\
"""Associates an event to an active agent.
		Example: an engineer, a performer, a composer...
        

		Relates an event to an active agent (a person, a computer, ... :-) )"""
propDocs["hasAgent"]=\
"""Associates an event to an active agent.
		Example: an engineer, a performer, a composer...
        

		Relates an event to an active agent (a person, a computer, ... :-) )"""
propDocs["hasFactor"]=\
"""Associates an event to a passive factor of it.
		Example: a flute, a musical score, a musical work...
	

		Relates an event to a passive factor (a tool, an instrument, an abstract cause...)"""
propDocs["hasFactor"]=\
"""Associates an event to a passive factor of it.
		Example: a flute, a musical score, a musical work...
	

		Relates an event to a passive factor (a tool, an instrument, an abstract cause...)"""
propDocs["hasLiteralFactor"]=\
"""Relates an event to a factor which can be described as a literal. This property
		should not be used as-is, but should be subsumed by other, more specific, properties
		(like an hypothetic :weatherCelsius, linking an event to a temperature)."""
propDocs["hasProduct"]=\
"""Associates an event to something it produces.
		Example: a sound, a score, a musical work...
        

		Relates an event to something produced during the event---a sound, a pie, whatever..."""
propDocs["hasProduct"]=\
"""Associates an event to something it produces.
		Example: a sound, a score, a musical work...
        

		Relates an event to something produced during the event---a sound, a pie, whatever..."""
propDocs["hasSubEvent"]=\
"""This property provides a way to split a complex event (for example, a performance involving several 
		musicians) into simpler ones (one event per musician).
		

		Allows to link an event to a sub-event. A sub-event might be an event split by time,
		space, agents, factors... This property can be used to express things such as "during
		this performance, this person was playing this instrument at this particular time", through 
		the creation of a sub-event, occuring at this given time, and having as agent the person and
		as factor the instrument"""
propDocs["hasSubEvent"]=\
"""This property provides a way to split a complex event (for example, a performance involving several 
		musicians) into simpler ones (one event per musician).
		

		Allows to link an event to a sub-event. A sub-event might be an event split by time,
		space, agents, factors... This property can be used to express things such as "during
		this performance, this person was playing this instrument at this particular time", through 
		the creation of a sub-event, occuring at this given time, and having as agent the person and
		as factor the instrument"""
propDocs["isAgentIn"]=\
"""Associates an agent to an event."""
propDocs["isAgentIn"]=\
"""Associates an agent to an event."""
propDocs["isFactorOf"]=\
"""Associates a factor to an event"""
propDocs["isFactorOf"]=\
"""Associates a factor to an event"""
propDocs["place"]=\
"""Associate an event with a place.

		The associated geographic object contains the actual geographic extent of the event.

		For example, linking an event to Paris, France, will specify that this event happened somewhere
		within this geographical object.
        

		Relates an event to a spatial object."""
propDocs["place"]=\
"""Associate an event with a place.

		The associated geographic object contains the actual geographic extent of the event.

		For example, linking an event to Paris, France, will specify that this event happened somewhere
		within this geographical object.
        

		Relates an event to a spatial object."""
propDocs["place"]=\
"""Associate an event with a place.

		The associated geographic object contains the actual geographic extent of the event.

		For example, linking an event to Paris, France, will specify that this event happened somewhere
		within this geographical object.
        

		Relates an event to a spatial object."""
propDocs["producedIn"]=\
"""Associates the product of an event to the event itself"""
propDocs["producedIn"]=\
"""Associates the product of an event to the event itself"""
propDocs["time"]=\
"""Associate an event with a time interval or a time instant.

		The associated time object contains the actual temporal extent of the event.

		For example, linking an event to the 9th of August, 2007, will specify that this event 
		happened during this day.
	

		Relates an event to a time object, classifying a time region (either instantaneous or having an extent).
		By using the Timeline ontology here, you can define event happening on a recorded track or on any 
		media with a temporal extent."""
propDocs["time"]=\
"""Associate an event with a time interval or a time instant.

		The associated time object contains the actual temporal extent of the event.

		For example, linking an event to the 9th of August, 2007, will specify that this event 
		happened during this day.
	

		Relates an event to a time object, classifying a time region (either instantaneous or having an extent).
		By using the Timeline ontology here, you can define event happening on a recorded track or on any 
		media with a temporal extent."""
propDocs["time"]=\
"""Associate an event with a time interval or a time instant.

		The associated time object contains the actual temporal extent of the event.

		For example, linking an event to the 9th of August, 2007, will specify that this event 
		happened during this day.
	

		Relates an event to a time object, classifying a time region (either instantaneous or having an extent).
		By using the Timeline ontology here, you can define event happening on a recorded track or on any 
		media with a temporal extent."""
propDocs["at"]=\
"""refers to a point or an interval on the time line, through an explicit datatype"""
propDocs["at"]=\
"""refers to a point or an interval on the time line, through an explicit datatype"""
propDocs["atDate"]=\
"""A subproperty of :at, allowing to address a date (beginning of it for an instant, all of it for an interval)"""
propDocs["atDateTime"]=\
"""This property links an instant defined on the universal time line to an XSD date/time value

		Place a time point on the universal time line by using xsd:dateTime."""
propDocs["atDateTime"]=\
"""This property links an instant defined on the universal time line to an XSD date/time value

		Place a time point on the universal time line by using xsd:dateTime."""
propDocs["atDateTime"]=\
"""This property links an instant defined on the universal time line to an XSD date/time value

		Place a time point on the universal time line by using xsd:dateTime."""
propDocs["atDuration"]=\
"""A property enabling to adress a time point P through the duration of the interval [0,P] on a continuous timeline

		Place a time point on an abstract time line by expressing its distance to
		the point 0, through xsd:duration (example: this instant is at 2s after 0 --> T2S)"""
propDocs["atDuration"]=\
"""A property enabling to adress a time point P through the duration of the interval [0,P] on a continuous timeline

		Place a time point on an abstract time line by expressing its distance to
		the point 0, through xsd:duration (example: this instant is at 2s after 0 --> T2S)"""
propDocs["atDuration"]=\
"""A property enabling to adress a time point P through the duration of the interval [0,P] on a continuous timeline

		Place a time point on an abstract time line by expressing its distance to
		the point 0, through xsd:duration (example: this instant is at 2s after 0 --> T2S)"""
propDocs["atInt"]=\
"""A subproperty of :at, having as a specific range xsd:int"""
propDocs["atReal"]=\
"""subproperty of :at, having xsd:float as a range"""
propDocs["atYear"]=\
"""A subproperty of :at, allowing to address a year (beginning of it for an instant, all of it for an interval)"""
propDocs["atYearMonth"]=\
"""A subproperty of :at, allowing to address a year/month (beginning of it for an instant, all of it for an interval)"""
propDocs["beginsAt"]=\
"""refers to the beginning of a time interval, through an explicit datatype. time:hasBeginning can be used as well, if you want to associate the beginning of the interval to an explicit time point resource"""
propDocs["beginsAtDateTime"]=\
"""Links an interval on a physical timeline to its actual start point,
		expressed using xsd:dateTime
	
A subproperty of :beginsAt, allowing to address the beginning of an interval as a date/time"""
propDocs["beginsAtDateTime"]=\
"""Links an interval on a physical timeline to its actual start point,
		expressed using xsd:dateTime
	
A subproperty of :beginsAt, allowing to address the beginning of an interval as a date/time"""
propDocs["beginsAtDateTime"]=\
"""Links an interval on a physical timeline to its actual start point,
		expressed using xsd:dateTime
	
A subproperty of :beginsAt, allowing to address the beginning of an interval as a date/time"""
propDocs["beginsAtDuration"]=\
"""Links an interval on a semi-infinite continuous time line to its
		start point, addressed using xsd:duration (duration between 0 and the
		start point)
	
A property enabling to adress a start time point P of an interval [P,E] through the duration of the interval [0,P] on a continuous timeline"""
propDocs["beginsAtDuration"]=\
"""Links an interval on a semi-infinite continuous time line to its
		start point, addressed using xsd:duration (duration between 0 and the
		start point)
	
A property enabling to adress a start time point P of an interval [P,E] through the duration of the interval [0,P] on a continuous timeline"""
propDocs["beginsAtDuration"]=\
"""Links an interval on a semi-infinite continuous time line to its
		start point, addressed using xsd:duration (duration between 0 and the
		start point)
	
A property enabling to adress a start time point P of an interval [P,E] through the duration of the interval [0,P] on a continuous timeline"""
propDocs["beginsAtInt"]=\
"""A subproperty of :beginsAt, having xsd:int as a range"""
propDocs["delay"]=\
"""associate a shift map to a particular delay"""
propDocs["delay"]=\
"""associate a shift map to a particular delay"""
propDocs["domainTimeLine"]=\
"""associates a timeline map to its domain timeline

		This property allows to associate a TimeLineMap with the first TimeLine it maps"""
propDocs["domainTimeLine"]=\
"""associates a timeline map to its domain timeline

		This property allows to associate a TimeLineMap with the first TimeLine it maps"""
propDocs["domainTimeLine"]=\
"""associates a timeline map to its domain timeline

		This property allows to associate a TimeLineMap with the first TimeLine it maps"""
propDocs["duration"]=\
"""the duration of a time interval"""
propDocs["durationInt"]=\
"""A subproperty of :duration, having xsd:int as a range"""
propDocs["durationXSD"]=\
"""A subproperty of :duration, having xsd:duration as a range

		Links an interval to its duration using xsd:duration"""
propDocs["durationXSD"]=\
"""A subproperty of :duration, having xsd:duration as a range

		Links an interval to its duration using xsd:duration"""
propDocs["durationXSD"]=\
"""A subproperty of :duration, having xsd:duration as a range

		Links an interval to its duration using xsd:duration"""
propDocs["endsAt"]=\
"""refers to the end of a time interval, through an explicit datatype. time:hasEnd can be used as well, if you want to associate the end of the interval to an explicit time point resource"""
propDocs["endsAtDateTime"]=\
"""A subproperty of :endsAt, allowing to address the end of an interval as a date/time"""
propDocs["endsAtDuration"]=\
"""A property enabling to adress an end time point P of an interval [S,P] through the duration of the interval [0,P] on a continuous timeline"""
propDocs["endsAtInt"]=\
"""A subproperty of :endsAt, having xsd:int as a range"""
propDocs["hopSize"]=\
"""hop size, associated to a uniform windowing map"""
propDocs["hopSize"]=\
"""hop size, associated to a uniform windowing map"""
propDocs["onTimeLine"]=\
"""Links an instant or an interval to the timeline it is defined on (eg. "1970 is defined on the
		time line universaltimeline", or "the interval between 0 and 2 minutes is defined on the time
		line backing this sound and this signal").
	

	Relates an interval or an instant to the timeline on which it is defined.

	The 29th of August, 2007 would be linked through this property to the universal timeline, whereas
	"from 2s to 5s on this particular signal" would be defined on the signal' timeline."""
propDocs["onTimeLine"]=\
"""Links an instant or an interval to the timeline it is defined on (eg. "1970 is defined on the
		time line universaltimeline", or "the interval between 0 and 2 minutes is defined on the time
		line backing this sound and this signal").
	

	Relates an interval or an instant to the timeline on which it is defined.

	The 29th of August, 2007 would be linked through this property to the universal timeline, whereas
	"from 2s to 5s on this particular signal" would be defined on the signal' timeline."""
propDocs["onTimeLine"]=\
"""Links an instant or an interval to the timeline it is defined on (eg. "1970 is defined on the
		time line universaltimeline", or "the interval between 0 and 2 minutes is defined on the time
		line backing this sound and this signal").
	

	Relates an interval or an instant to the timeline on which it is defined.

	The 29th of August, 2007 would be linked through this property to the universal timeline, whereas
	"from 2s to 5s on this particular signal" would be defined on the signal' timeline."""
propDocs["origin"]=\
"""associate an origin map to its origin on the domain physical timeline"""
propDocs["origin"]=\
"""associate an origin map to its origin on the domain physical timeline"""
propDocs["originAt"]=\
"""This property specifies, for an OriginMap, the time point on the physical time line
		0 on a RelativeTimeLine is equivalent to."""
propDocs["originAt"]=\
"""This property specifies, for an OriginMap, the time point on the physical time line
		0 on a RelativeTimeLine is equivalent to."""
propDocs["rangeTimeLine"]=\
"""This property allows to associate a TimeLineMap with the second TimeLine it maps
        
associates a timeline map to its range timeline"""
propDocs["rangeTimeLine"]=\
"""This property allows to associate a TimeLineMap with the second TimeLine it maps
        
associates a timeline map to its range timeline"""
propDocs["rangeTimeLine"]=\
"""This property allows to associate a TimeLineMap with the second TimeLine it maps
        
associates a timeline map to its range timeline"""
propDocs["sampleRate"]=\
"""associates a sample rate value to a uniform sampling map"""
propDocs["sampleRate"]=\
"""associates a sample rate value to a uniform sampling map"""
propDocs["windowLength"]=\
"""window length, associated to a uniform windowing map"""
propDocs["windowLength"]=\
"""window length, associated to a uniform windowing map"""
propDocs["creator"]=\
"""An entity primarily responsible for making 
		        the resource."""
propDocs["date"]=""
propDocs["description"]=\
"""An account of the resource."""
propDocs["description"]=\
"""An account of the resource."""
propDocs["title"]=\
"""A name given to the resource."""
propDocs["title"]=\
"""A name given to the resource."""
propDocs["base_chord"]=\
"""The chord on which this one is based. 
			For example, a C7 chord might have chord:Cmaj as its base chord."""
propDocs["bass"]=\
"""The bass note of the chord (indicates the inversion)."""
propDocs["chord"]=\
"""The chord associated with a chord event."""
propDocs["degree"]=\
"""The degree of an interval based on the root of a chord."""
propDocs["interval"]=\
"""An interval from the root which is part of the chord."""
propDocs["modifier"]=\
"""A modification to a note's pitch."""
propDocs["natural"]=\
"""The natural from which this note is derived."""
propDocs["root"]=\
"""The root note of the chord."""
propDocs["semitone_interval"]=\
"""An interval measured in semitones."""
propDocs["without_interval"]=\
"""A degree of the scale expected in the chord but not actually present here."""
propDocs["amazon_asin"]=\
"""Used to link a work or the expression of a work to its corresponding Amazon ASINs page."""
propDocs["amazon_asin"]=\
"""Used to link a work or the expression of a work to its corresponding Amazon ASINs page."""
propDocs["arranged_in"]=\
"""Associates a work to an arrangement event where it was arranged"""
propDocs["arrangement_of"]=\
"""Associates an arrangement event to a work"""
propDocs["available_as"]=\
"""Relates a musical manifestation to a musical item (this album, and my particular cd). By using
		this property, there is no assumption on wether the full content is available on the linked item.
		To be explicit about this, you can use a sub-property, such as mo:item (the full manifestation
		is available on that item) or mo:preview (only a part of the manifestation is available on
		that item).

		This is a subproperty of frbr:examplar."""
propDocs["biography"]=\
"""Used to link an artist to their online biography."""
propDocs["biography"]=\
"""Used to link an artist to their online biography."""
propDocs["bitsPerSample"]=\
"""Associates a digital signal to the number a bits used to encode one sample. Range is xsd:int."""
propDocs["bitsPerSample"]=\
"""Associates a digital signal to the number a bits used to encode one sample. Range is xsd:int."""
propDocs["bpm"]=\
"""Indicates the BPM of a MusicalWork or a particular Performance 
		Beats per minute: the pace of music measured by the number of beats occurring in 60 seconds."""
propDocs["channels"]=\
"""Associates a signal to the number of channels it holds (mono --> 1, stereo --> 2). Range is xsd:int."""
propDocs["channels"]=\
"""Associates a signal to the number of channels it holds (mono --> 1, stereo --> 2). Range is xsd:int."""
propDocs["collaborated_with"]=\
"""Used to relate two collaborating people on a work."""
propDocs["collaborated_with"]=\
"""Used to relate two collaborating people on a work."""
propDocs["compilation_of"]=\
"""Indicates that a musical manifestation is a compilation of several Signals."""
propDocs["compilation_of"]=\
"""Indicates that a musical manifestation is a compilation of several Signals."""
propDocs["compiled"]=\
"""Used to relate an person or a group of person who compiled the manifestation of a musical work."""
propDocs["compiled"]=\
"""Used to relate an person or a group of person who compiled the manifestation of a musical work."""
propDocs["compiler"]=\
"""Used to relate the manifestation of a musical work to a person or a group of person who compiled it."""
propDocs["compiler"]=\
"""Used to relate the manifestation of a musical work to a person or a group of person who compiled it."""
propDocs["composed_in"]=\
"""Associates a MusicalWork to the Composition event pertaining
		to its creation. For example, I might use this property to associate
		the Magic Flute to its composition event, occuring during 1782 and having as
		a mo:composer Mozart."""
propDocs["composer"]=\
"""Associates a composition event to the actual composer. For example,
		this property could link the event corresponding to the composition of the
		Magic Flute in 1782 to Mozart himself (who obviously has a FOAF profile:-) )."""
propDocs["conducted"]=\
"""Relates agents to the performances they were conducting"""
propDocs["conducted"]=\
"""Relates agents to the performances they were conducting"""
propDocs["conductor"]=\
"""Relates a performance to the conductor involved"""
propDocs["conductor"]=\
"""Relates a performance to the conductor involved"""
propDocs["contains_sample_from"]=\
"""Relates a signal to another signal, which has been sampled."""
propDocs["discography"]=\
"""Used to links an artist to an online discography of their musical works. The discography should provide a summary of each released musical work of the artist."""
propDocs["discography"]=\
"""Used to links an artist to an online discography of their musical works. The discography should provide a summary of each released musical work of the artist."""
propDocs["discogs"]=\
"""Used to link a musical work or the expression of a musical work, an artist or a corporate body to to its corresponding Discogs page."""
propDocs["discogs"]=\
"""Used to link a musical work or the expression of a musical work, an artist or a corporate body to to its corresponding Discogs page."""
propDocs["djmix_of"]=\
"""Indicates that all (or most of) the tracks of a musical work or the expression of a musical work were mixed together from all (or most of) the tracks from another musical work or the expression of a musical work to form a so called DJ-Mix. 
    
The tracks might have been altered by pitching (so that the tempo of one track matches the tempo of the following track) and fading (so that one track blends in smoothly with the other). If the tracks have been more substantially altered, the "mo:remix" relationship type is more appropriate."""
propDocs["djmix_of"]=\
"""Indicates that all (or most of) the tracks of a musical work or the expression of a musical work were mixed together from all (or most of) the tracks from another musical work or the expression of a musical work to form a so called DJ-Mix. 
    
The tracks might have been altered by pitching (so that the tempo of one track matches the tempo of the following track) and fading (so that one track blends in smoothly with the other). If the tracks have been more substantially altered, the "mo:remix" relationship type is more appropriate."""
propDocs["djmixed"]=\
"""Used to relate an artist who djmixed a musical work or the expression of a musical work. 
    
The artist usually selected the tracks, chose their sequence, and slightly changed them by fading (so that one track blends in smoothly with the other) or pitching (so that the tempo of one track matches the tempo of the following track). This applies to a 'Mixtape' in which all tracks were DJ-mixed together into one single long track."""
propDocs["djmixed"]=\
"""Used to relate an artist who djmixed a musical work or the expression of a musical work. 
    
The artist usually selected the tracks, chose their sequence, and slightly changed them by fading (so that one track blends in smoothly with the other) or pitching (so that the tempo of one track matches the tempo of the following track). This applies to a 'Mixtape' in which all tracks were DJ-mixed together into one single long track."""
propDocs["djmixed_by"]=\
"""Used to relate a work or the expression of a work to an artist who djmixed it. 
    
The artist usually selected the tracks, chose their sequence, and slightly changed them by fading (so that one track blends in smoothly with the other) or pitching (so that the tempo of one track matches the tempo of the following track). This applies to a 'Mixtape' in which all tracks were DJ-mixed together into one single long track."""
propDocs["djmixed_by"]=\
"""Used to relate a work or the expression of a work to an artist who djmixed it. 
    
The artist usually selected the tracks, chose their sequence, and slightly changed them by fading (so that one track blends in smoothly with the other) or pitching (so that the tempo of one track matches the tempo of the following track). This applies to a 'Mixtape' in which all tracks were DJ-mixed together into one single long track."""
propDocs["download"]=\
"""This property can be used to link from a person to the website where they make their works available, or from
                a manifestation (a track or an album, for example) to a web page where it is available for
                download.
		
		It is better to use one of the three sub-properties instead of this one in order to specify wether the
		content can be accessed for free (mo:freedownload), if it is just free preview material (mo:previewdownload), or
		if it can be accessed for some money (mo:paiddownload) (this includes links to the Amazon store, for example).

                This property MUST be used only if the content is just available through a web page (holding, for example
                a Flash application) - it is better to link to actual content directly through the use of mo:availableAs and
                mo:Stream, mo:Torrent or mo:ED2K, etc. Therefore, Semantic Web user agents that don't know how to read HTML and even
                less to rip streams from Flash applications can still access the audio content."""
propDocs["download"]=\
"""This property can be used to link from a person to the website where they make their works available, or from
                a manifestation (a track or an album, for example) to a web page where it is available for
                download.
		
		It is better to use one of the three sub-properties instead of this one in order to specify wether the
		content can be accessed for free (mo:freedownload), if it is just free preview material (mo:previewdownload), or
		if it can be accessed for some money (mo:paiddownload) (this includes links to the Amazon store, for example).

                This property MUST be used only if the content is just available through a web page (holding, for example
                a Flash application) - it is better to link to actual content directly through the use of mo:availableAs and
                mo:Stream, mo:Torrent or mo:ED2K, etc. Therefore, Semantic Web user agents that don't know how to read HTML and even
                less to rip streams from Flash applications can still access the audio content."""
propDocs["encodes"]=\
"""Relates a MusicalItem (a track on a particular CD, an audio file, a stream somewhere) to the signal it encodes.

		This is usually a lower-resolution version of the master signal (issued from a Recording event)."""
propDocs["encoding"]=\
"""Method used to convert analog electronic signals into digital format such as "MP3 CBR @ 128kbps", "OGG @ 160kbps", "FLAC", etc."""
propDocs["engineer"]=\
"""Relates a performance or a recording to the engineer involved"""
propDocs["engineer"]=\
"""Relates a performance or a recording to the engineer involved"""
propDocs["engineered"]=\
"""Relates agents to the performances/recordings they were engineering in"""
propDocs["engineered"]=\
"""Relates agents to the performances/recordings they were engineering in"""
propDocs["event_homepage"]=\
"""Links a particular event to a web page"""
propDocs["exchange_item"]=\
"""A person, a group of person or an organization exchanging an exemplar of a single manifestation."""
propDocs["fanpage"]=\
"""Used to link an artist to a fan-created webpage devoted to that artist."""
propDocs["fanpage"]=\
"""Used to link an artist to a fan-created webpage devoted to that artist."""
propDocs["free_download"]=\
"""This property can be used to link from a person to the website where they make their works available, or from
		a manifestation (a track or an album, for example) to a web page where it is available for free 
		download.

		This property MUST be used only if the content is just available through a web page (holding, for example
		a Flash application) - it is better to link to actual content directly through the use of mo:availableAs and 
		mo:Stream, mo:Torrent or mo:ED2K, etc. Therefore, Semantic Web user agents that don't know how to read HTML and even
		less to rip streams from Flash applications can still access the audio content."""
propDocs["free_download"]=\
"""This property can be used to link from a person to the website where they make their works available, or from
		a manifestation (a track or an album, for example) to a web page where it is available for free 
		download.

		This property MUST be used only if the content is just available through a web page (holding, for example
		a Flash application) - it is better to link to actual content directly through the use of mo:availableAs and 
		mo:Stream, mo:Torrent or mo:ED2K, etc. Therefore, Semantic Web user agents that don't know how to read HTML and even
		less to rip streams from Flash applications can still access the audio content."""
propDocs["genre"]=\
"""Associates an event (like a performance or a recording) to a particular musical genre.
		Further version of this property may also include works and scores in the domain."""
propDocs["has_movement"]=\
"""Indicates that a musical work has movements"""
propDocs["image"]=\
"""Indicates a pictorial image (JPEG, GIF, PNG, Etc.) of a musical work, the expression of a musical work, the manifestation of a work or the examplar of a manifestation."""
propDocs["imdb"]=\
"""Used to link an artist, a musical work or the expression of a musical work to their equivalent page on IMDb, the InternetMovieDatabase."""
propDocs["imdb"]=\
"""Used to link an artist, a musical work or the expression of a musical work to their equivalent page on IMDb, the InternetMovieDatabase."""
propDocs["instrument"]=\
"""Relates a performance to a musical instrument involved"""
propDocs["isrc"]=\
"""The ISRC (International Standard Recording Code) is the international identification system for sound recordings and music videorecordings. 
	Each ISRC is a unique and permanent identifier for a specific recording which can be permanently encoded into a product as its digital fingerprint. 
	Encoded ISRC provide the means to automatically identify recordings for royalty payments."""
propDocs["item"]=\
"""Relates a musical manifestation to a musical item (this album, and my particular cd) holding the
		entire manifestation, and not just a part of it."""
propDocs["key"]=\
"""Indicated the key used by the musicians during a performance, or the key of a MusicalWork.
		Any of 24 major or minor diatonic scales that provide the tonal framework for a piece of music."""
propDocs["level"]=\
"""This annotation property associates to a particular Music Ontology term the corresponding
		expressiveness level. These levels can be:

			- 1: Only editorial/Musicbrainz type information
			- 2: Workflow information
			- 3: Even decomposition
		
		This property is mainly used for specification generation."""
propDocs["licence"]=\
"""Used to link a work or the expression of a work to the license under which they can be manipulated (downloaded, modified, etc). 
    
This is usually used to link to a Creative Commons licence."""
propDocs["licence"]=\
"""Used to link a work or the expression of a work to the license under which they can be manipulated (downloaded, modified, etc). 
    
This is usually used to link to a Creative Commons licence."""
propDocs["listened"]=\
"""Relates agents to the performances they were listening in"""
propDocs["listened"]=\
"""Relates agents to the performances they were listening in"""
propDocs["listener"]=\
"""Relates a performance to the listener involved"""
propDocs["listener"]=\
"""Relates a performance to the listener involved"""
propDocs["mailorder"]=\
"""Used to link a musical work or the expression of a musical work to a website where people can buy a copy of the musical manifestation."""
propDocs["mailorder"]=\
"""Used to link a musical work or the expression of a musical work to a website where people can buy a copy of the musical manifestation."""
propDocs["manifestation"]=\
"""Links a MusicalExpression to its manifestations, subproperty of frbr:embodiment"""
propDocs["mashup_of"]=\
"""Indicates that musical works or the expressions of a musical work were mashed up on this album or track. 
    
This means that two musical works or the expressions of a musical work by different artists are mixed together, over each other, or otherwise combined into a single musical work (usually by a third artist, the remixer)."""
propDocs["mashup_of"]=\
"""Indicates that musical works or the expressions of a musical work were mashed up on this album or track. 
    
This means that two musical works or the expressions of a musical work by different artists are mixed together, over each other, or otherwise combined into a single musical work (usually by a third artist, the remixer)."""
propDocs["medley_of"]=\
"""Indicates that a musical expression is a medley of several other musical expressions. 
    
This means that the orignial musical expression were rearranged to create a new musical expression in the form of a medley."""
propDocs["medley_of"]=\
"""Indicates that a musical expression is a medley of several other musical expressions. 
    
This means that the orignial musical expression were rearranged to create a new musical expression in the form of a medley."""
propDocs["member_of"]=\
"""Inverse of the foaf:member property"""
propDocs["member_of"]=\
"""Inverse of the foaf:member property"""
propDocs["movementNum"]=""
propDocs["movement_number"]=\
"""Indicates the position of a movement in a musical work."""
propDocs["musicbrainz"]=\
"""Linking an agent, a track or a record to its corresponding Musicbrainz page."""
propDocs["musicbrainz"]=\
"""Linking an agent, a track or a record to its corresponding Musicbrainz page."""
propDocs["musicmoz"]=\
"""Used to link an artist, a musical work or the expression of a musical work to its corresponding MusicMoz page."""
propDocs["musicmoz"]=\
"""Used to link an artist, a musical work or the expression of a musical work to its corresponding MusicMoz page."""
propDocs["myspace"]=\
"""Used to link a person to its corresponding MySpace page."""
propDocs["myspace"]=\
"""Used to link a person to its corresponding MySpace page."""
propDocs["olga"]=\
"""Used to link a track to a tabulature file for track in the On-Line Guitar Archive."""
propDocs["olga"]=\
"""Used to link a track to a tabulature file for track in the On-Line Guitar Archive."""
propDocs["onlinecommunity"]=\
"""Used to link a person with an online community web page like a blog, a wiki, a forum, a livejournal page, Etc."""
propDocs["onlinecommunity"]=\
"""Used to link a person with an online community web page like a blog, a wiki, a forum, a livejournal page, Etc."""
propDocs["opus"]=\
"""Used to define a creative work, especially a musical composition numbered to designate the order of a composer's works."""
propDocs["other_release_of"]=\
"""Indicates that two musical manifestations are essentially the same."""
propDocs["other_release_of"]=\
"""Indicates that two musical manifestations are essentially the same."""
propDocs["paid_download"]=\
"""Provide a link from an artist to a web page where all of that artist's musical work is available for some money,
                or a link from a manifestation (record/track, for example) to a web page providing a paid access to this manifestation."""
propDocs["paid_download"]=\
"""Provide a link from an artist to a web page where all of that artist's musical work is available for some money,
                or a link from a manifestation (record/track, for example) to a web page providing a paid access to this manifestation."""
propDocs["performance_of"]=\
"""Associates a Performance to a musical work or an arrangement that is being used as a factor in it.
		For example, I might use this property to attach the Magic Flute musical work to 
		a particular Performance."""
propDocs["performed"]=\
"""Relates agents to the performances they were performing in"""
propDocs["performed"]=\
"""Relates agents to the performances they were performing in"""
propDocs["performed_in"]=\
"""Associates a Musical Work or an Score to Performances in which they were
		a factor. For example, I might use this property in order to 
		associate the Magic Flute to a particular performance at the Opera
		Bastille last year."""
propDocs["performer"]=\
"""Relates a performance to the performers involved"""
propDocs["performer"]=\
"""Relates a performance to the performers involved"""
propDocs["possess_item"]=\
"""A person, a group of person or an organization possessing an exemplar of a single manifestation."""
propDocs["preview"]=\
"""Relates a musical manifestation to a musical item (this album, and my particular cd), which holds
		a preview of the manifestation (eg. one track for an album, or a snippet for a track)"""
propDocs["preview_download"]=\
"""This property can be used to link from a person to the website where they make previews of their works available, or from
                a manifestation (a track or an album, for example) to a web page where a preview download is available.

                This property MUST be used only if the content is just available through a web page (holding, for example
                a Flash application) - it is better to link to actual content directly through the use of mo:availableAs and
                mo:Stream, mo:Torrent or mo:ED2K, etc. Therefore, Semantic Web user agents that don't know how to read HTML and even
                less to rip streams from Flash applications can still access the audio content."""
propDocs["preview_download"]=\
"""This property can be used to link from a person to the website where they make previews of their works available, or from
                a manifestation (a track or an album, for example) to a web page where a preview download is available.

                This property MUST be used only if the content is just available through a web page (holding, for example
                a Flash application) - it is better to link to actual content directly through the use of mo:availableAs and
                mo:Stream, mo:Torrent or mo:ED2K, etc. Therefore, Semantic Web user agents that don't know how to read HTML and even
                less to rip streams from Flash applications can still access the audio content."""
propDocs["produced"]=\
"""Used to relate an person or a group of person who produced the manifestation of a work."""
propDocs["produced"]=\
"""Used to relate an person or a group of person who produced the manifestation of a work."""
propDocs["produced_score"]=\
"""Associates an arrangement event to a score product (score here does not refer to a published score, but more
		an abstract arrangement of a particular work)."""
propDocs["produced_signal"]=\
"""Associates a Recording to the outputted signal."""
propDocs["produced_sound"]=\
"""Associates a Performance to a physical Sound that is being produced by it."""
propDocs["produced_work"]=\
"""Associates a composition event to the produced MusicalWork. For example,
                this property could link the event corresponding to the composition of the
                Magic Flute in 1782 to the Magic Flute musical work itself. This musical work
		can then be used in particular performances."""
propDocs["producer"]=\
"""Used to relate the manifestation of a work to a person or a group of person who produced it."""
propDocs["producer"]=\
"""Used to relate the manifestation of a work to a person or a group of person who produced it."""
propDocs["producesWork"]=""
propDocs["publication_of"]=\
"""Link a particular manifestation to the related signal, score, libretto, or lyrics"""
propDocs["published"]=\
"""Used to relate an person or a group of person who published the manifestation of a work."""
propDocs["published"]=\
"""Used to relate an person or a group of person who published the manifestation of a work."""
propDocs["published_as"]=\
"""Links a signal or a score to its manifestations - this is a subproperty of frbr:embodiment (linking
		an Expression to a Manifestation)"""
propDocs["publisher"]=\
"""Used to relate a musical manifestation to a person or a group of person who published it."""
propDocs["publisher"]=\
"""Used to relate a musical manifestation to a person or a group of person who published it."""
propDocs["publishing_location"]=\
"""Relates a musical manifestation to its publication location."""
propDocs["puid"]=\
"""Link a signal to the PUIDs associated with it, that is, PUID computed from MusicalItems (mo:AudioFile) 
		derived from this signal.

		PUIDs (Portable Unique IDentifier) are the IDs used in the 
		proprietary MusicDNS AudioFingerprinting system which is operated by MusicIP.

		Using PUIDs, one (with some luck) can identify the Signal object associated with a particular audio file, therefore allowing
		to access further information (on which release this track is featured? etc.). Using some more metadata one can identify
		the particular Track corresponding to the audio file (a track on a particular release)."""
propDocs["recordedAs"]=""
propDocs["recordedAs"]=""
propDocs["recorded_as"]=\
"""This is a shortcut property, allowing to bypass all the Sound/Recording steps. This property
		allows to directly link a Performance to the recorded Signal. This is recommended for "normal"
		users. However, advanced users wanting to express things such as the location of the microphone will
		have to create this shortcut as well as the whole workflow, in order to let the "normal" users access
		simply the, well, simple information:-) ."""
propDocs["recorded_in"]=\
"""Associates a physical Sound to a Recording event where it is being used 
		in order to produce a signal. For example, I might use this property to 
		associate the sound produced by a particular performance of the magic flute
		to a given recording, done using my cell-phone."""
propDocs["recording_of"]=\
"""Associates a Recording event to a physical Sound being recorded.
                For example, I might use this property to
                associate a given recording, done using my cell phone, to the 
		sound produced by a particular performance of the magic flute."""
propDocs["records"]=\
"""This is the inverse of the shortcut property recordedAs, allowing to relate directly a performance
		to a signal."""
propDocs["records"]=\
"""This is the inverse of the shortcut property recordedAs, allowing to relate directly a performance
		to a signal."""
propDocs["release_status"]=\
"""Relates a musical manifestation to its release status (bootleg, ...)"""
propDocs["release_type"]=\
"""Relates a musical manifestation to its release type (interview, spoken word, album, ...)"""
propDocs["remaster_of"]=\
"""This relates two musical work or the expression of a musical work, where one is a remaster of the other. 
    
A remaster is a new version made for release from source recordings that were earlier released separately. This is usually done to improve the audio quality or adjust for more modern playback equipment. The process generally doesn't involve changing the music in any artistically important way. It may, however, result in tracks that are a few seconds longer or shorter."""
propDocs["remaster_of"]=\
"""This relates two musical work or the expression of a musical work, where one is a remaster of the other. 
    
A remaster is a new version made for release from source recordings that were earlier released separately. This is usually done to improve the audio quality or adjust for more modern playback equipment. The process generally doesn't involve changing the music in any artistically important way. It may, however, result in tracks that are a few seconds longer or shorter."""
propDocs["remix_of"]=\
"""Used to relate the remix of a musical work in a substantially altered version produced by mixing together individual tracks or segments of an original musical source work."""
propDocs["remix_of"]=\
"""Used to relate the remix of a musical work in a substantially altered version produced by mixing together individual tracks or segments of an original musical source work."""
propDocs["remixed"]=\
"""Used to relate an artist who remixed a musical work or the expression of a musical work. 
    
This involves taking just one other musical work and using audio editing to make it sound like a significantly different, but usually still recognisable, song. It can be used to link an artist to a single song that they remixed, or, if they remixed an entire musical work."""
propDocs["remixed"]=\
"""Used to relate an artist who remixed a musical work or the expression of a musical work. 
    
This involves taking just one other musical work and using audio editing to make it sound like a significantly different, but usually still recognisable, song. It can be used to link an artist to a single song that they remixed, or, if they remixed an entire musical work."""
propDocs["remixer"]=\
"""Used to relate a musical work or the expression of a musical work to an artist who remixed it. 
    
This involves taking just one other musical work and using audio editing to make it sound like a significantly different, but usually still recognisable, song. It can be used to link an artist to a single song that they remixed, or, if they remixed an entire musical work."""
propDocs["remixer"]=\
"""Used to relate a musical work or the expression of a musical work to an artist who remixed it. 
    
This involves taking just one other musical work and using audio editing to make it sound like a significantly different, but usually still recognisable, song. It can be used to link an artist to a single song that they remixed, or, if they remixed an entire musical work."""
propDocs["review"]=\
"""Used to link a work or the expression of a work to a review. 
    
The review does not have to be open content, as long as it is accessible to the general internet population."""
propDocs["review"]=\
"""Used to link a work or the expression of a work to a review. 
    
The review does not have to be open content, as long as it is accessible to the general internet population."""
propDocs["sample_rate"]=\
"""Associates a digital signal to its sample rate. It might be easier to express it this way instead of
		defining a timeline map:-) Range is xsd:float."""
propDocs["sample_rate"]=\
"""Associates a digital signal to its sample rate. It might be easier to express it this way instead of
		defining a timeline map:-) Range is xsd:float."""
propDocs["sampled"]=\
"""Used to relate an artist who sampled a Signal."""
propDocs["sampled"]=\
"""Used to relate an artist who sampled a Signal."""
propDocs["sampled_version"]=\
"""Associates an analog signal with a sampled version of it"""
propDocs["sampled_version_of"]=\
"""Associates a digital signal with the analog version of it"""
propDocs["sampled_version_of"]=\
"""Associates a digital signal with the analog version of it"""
propDocs["sampler"]=\
"""Used to relate the manifestation of a musical work to an artist who sampled it."""
propDocs["sampler"]=\
"""Used to relate the manifestation of a musical work to an artist who sampled it."""
propDocs["sell_item"]=\
"""A person, a group of person or an organization selling an exemplar of a single manifestation."""
propDocs["similar_to"]=\
"""A similarity relationships between two objects (so far, either an agent, a signal or a genre, but
		this could grow).
		This relationship is pretty general and doesn't make any assumptions on how the similarity claim
		was derived.
		Such similarity statements can come from a range of different sources (Musicbrainz similarities between
		artists, or coming from some automatic content analysis).
		However, the origin of such statements should be kept using a named graph approach - and ultimately, the 
		documents providing such statements should attach some metadata to themselves (confidence of the claim, etc.)."""
propDocs["similar_to"]=\
"""A similarity relationships between two objects (so far, either an agent, a signal or a genre, but
		this could grow).
		This relationship is pretty general and doesn't make any assumptions on how the similarity claim
		was derived.
		Such similarity statements can come from a range of different sources (Musicbrainz similarities between
		artists, or coming from some automatic content analysis).
		However, the origin of such statements should be kept using a named graph approach - and ultimately, the 
		documents providing such statements should attach some metadata to themselves (confidence of the claim, etc.)."""
propDocs["supporting_musician"]=\
"""Used to relate an artist doing long-time instrumental or vocal support for another artist."""
propDocs["supporting_musician"]=\
"""Used to relate an artist doing long-time instrumental or vocal support for another artist."""
propDocs["tempo"]=\
"""Rate of speed or pace of music. Tempo markings are traditionally given in Italian; 
		common markings include: grave (solemn; very, very slow); largo (broad; very slow); 
		adagio (quite slow); andante (a walking pace); moderato (moderate); allegro (fast; cheerful); 
		vivace (lively); presto (very fast); accelerando (getting faster); ritardando (getting slower); 
		and a tempo (in time; returning to the original pace)."""
propDocs["time"]=\
"""Associates a Signal to a time object - its actual domain"""
propDocs["time"]=\
"""Associates a Signal to a time object - its actual domain"""
propDocs["track"]=\
"""Indicates a part of a musical manifestation - in this particular case, a track."""
propDocs["track_number"]=\
"""Indicates the position of a track on a record medium (a CD, etc.)."""
propDocs["translation_of"]=\
"""Indicates that a work or the expression of a work has translated or transliterated into another expression of a work."""
propDocs["translation_of"]=\
"""Indicates that a work or the expression of a work has translated or transliterated into another expression of a work."""
propDocs["tribute_to"]=\
"""Indicates a musical work or the expression of a musical work that is a tribute to an artist - normally consisting of music being composed by the artist but performed by other artists."""
propDocs["tribute_to"]=\
"""Indicates a musical work or the expression of a musical work that is a tribute to an artist - normally consisting of music being composed by the artist but performed by other artists."""
propDocs["trmid"]=\
"""Indicates the TRMID of a track.
		TRM IDs are MusicBrainz' old AudioFingerprinting system. 
		TRM (TRM Recognizes Music) IDs are (somewhat) unique ids that represent 
		the audio signature of a musical piece (see AudioFingerprint)."""
propDocs["want_item"]=\
"""A person, a group of person or an organization wanting an exemplar of a single manifestation."""
propDocs["wikipedia"]=\
"""Used to link an work, an expression of a work, a manifestation of a work, 
		a person, an instrument or a musical genre to its corresponding WikiPedia page. 
		The full URL should be used, not just the WikiName."""
propDocs["wikipedia"]=\
"""Used to link an work, an expression of a work, a manifestation of a work, 
		a person, an instrument or a musical genre to its corresponding WikiPedia page. 
		The full URL should be used, not just the WikiName."""
propDocs["comment"]=""
propDocs["isDefinedBy"]=""
propDocs["label"]=\
"""A human-readable name for the subject."""
propDocs["label"]=\
"""A human-readable name for the subject."""
propDocs["seeAlso"]=""
propDocs["allValuesFrom"]=""
propDocs["backwardCompatibleWith"]=""
propDocs["backwardCompatibleWith"]=""
propDocs["cardinality"]=""
propDocs["complementOf"]=""
propDocs["differentFrom"]=""
propDocs["disjointWith"]=""
propDocs["distinctMembers"]=""
propDocs["equivalentClass"]=""
propDocs["equivalentProperty"]=""
propDocs["hasValue"]=""
propDocs["imports"]=""
propDocs["imports"]=""
propDocs["incompatibleWith"]=""
propDocs["incompatibleWith"]=""
propDocs["intersectionOf"]=""
propDocs["inverseOf"]=""
propDocs["maxCardinality"]=""
propDocs["minCardinality"]=""
propDocs["onProperty"]=""
propDocs["oneOf"]=""
propDocs["priorVersion"]=""
propDocs["priorVersion"]=""
propDocs["sameAs"]=""
propDocs["someValuesFrom"]=""
propDocs["unionOf"]=""
propDocs["versionInfo"]=""
propDocs["versionInfo"]=""
propDocs["term_status"]=""
propDocs["after"]=""
propDocs["before"]=""
propDocs["day"]=""
propDocs["dayOfWeek"]=""
propDocs["dayOfYear"]=""
propDocs["days"]=""
propDocs["hasBeginning"]=""
propDocs["hasDateTimeDescription"]=""
propDocs["hasDurationDescription"]=""
propDocs["hasEnd"]=""
propDocs["hour"]=""
propDocs["hours"]=""
propDocs["inDateTime"]=""
propDocs["inXSDDateTime"]=""
propDocs["inside"]=""
propDocs["intervalAfter"]=""
propDocs["intervalBefore"]=\
"""One of Allen's relations. Specifies that an interval is before an other."""
propDocs["intervalBefore"]=\
"""One of Allen's relations. Specifies that an interval is before an other."""
propDocs["intervalContains"]=""
propDocs["intervalDuring"]=\
"""One of Allen's relations. Specifies that an interval occurs during an other.
		It is really handy to express things like "it happened the 15th of august, but I do not remember exactly when"."""
propDocs["intervalDuring"]=\
"""One of Allen's relations. Specifies that an interval occurs during an other.
		It is really handy to express things like "it happened the 15th of august, but I do not remember exactly when"."""
propDocs["intervalEquals"]=""
propDocs["intervalFinishedBy"]=""
propDocs["intervalFinishes"]=""
propDocs["intervalMeets"]=\
"""One of Allen's relations. Specifies that an interval meets an other one."""
propDocs["intervalMeets"]=\
"""One of Allen's relations. Specifies that an interval meets an other one."""
propDocs["intervalMetBy"]=""
propDocs["intervalOverlappedBy"]=""
propDocs["intervalOverlaps"]=""
propDocs["intervalStartedBy"]=""
propDocs["intervalStarts"]=""
propDocs["minute"]=""
propDocs["minutes"]=""
propDocs["month"]=""
propDocs["months"]=""
propDocs["second"]=""
propDocs["seconds"]=""
propDocs["timeZone"]=""
propDocs["unitType"]=""
propDocs["week"]=""
propDocs["weeks"]=""
propDocs["xsdDateTime"]=""
propDocs["year"]=""
propDocs["years"]=""
propDocs["accountName"]=\
"""Indicates the name (identifier) associated with this online account."""
propDocs["accountName"]=\
"""Indicates the name (identifier) associated with this online account."""
propDocs["accountServiceHomepage"]=\
"""Indicates a homepage of the service provide for this online account."""
propDocs["accountServiceHomepage"]=\
"""Indicates a homepage of the service provide for this online account."""
propDocs["aimChatID"]=\
"""An AIM chat ID"""
propDocs["aimChatID"]=\
"""An AIM chat ID"""
propDocs["based_near"]=\
"""A location that something is based near, for some broadly human notion of near."""
propDocs["based_near"]=\
"""A location that something is based near, for some broadly human notion of near."""
propDocs["birthday"]=\
"""The birthday of this Agent, represented in mm-dd string form, eg. '12-31'."""
propDocs["birthday"]=\
"""The birthday of this Agent, represented in mm-dd string form, eg. '12-31'."""
propDocs["birthday"]=\
"""The birthday of this Agent, represented in mm-dd string form, eg. '12-31'."""
propDocs["currentProject"]=\
"""A current project this person works on."""
propDocs["currentProject"]=\
"""A current project this person works on."""
propDocs["depiction"]=\
"""A depiction of some thing."""
propDocs["depiction"]=\
"""A depiction of some thing."""
propDocs["depicts"]=\
"""A thing depicted in this representation."""
propDocs["depicts"]=\
"""A thing depicted in this representation."""
propDocs["dnaChecksum"]=\
"""A checksum for the DNA of some thing. Joke."""
propDocs["dnaChecksum"]=\
"""A checksum for the DNA of some thing. Joke."""
propDocs["family_name"]=\
"""The family_name of some person."""
propDocs["family_name"]=\
"""The family_name of some person."""
propDocs["firstName"]=\
"""The first name of a person."""
propDocs["firstName"]=\
"""The first name of a person."""
propDocs["fundedBy"]=\
"""An organization funding a project or person."""
propDocs["fundedBy"]=\
"""An organization funding a project or person."""
propDocs["geekcode"]=\
"""A textual geekcode for this person, see http://www.geekcode.com/geek.html"""
propDocs["geekcode"]=\
"""A textual geekcode for this person, see http://www.geekcode.com/geek.html"""
propDocs["gender"]=\
"""The gender of this Agent (typically but not necessarily 'male' or 'female')."""
propDocs["gender"]=\
"""The gender of this Agent (typically but not necessarily 'male' or 'female')."""
propDocs["gender"]=\
"""The gender of this Agent (typically but not necessarily 'male' or 'female')."""
propDocs["givenname"]=\
"""The given name of some person."""
propDocs["givenname"]=\
"""The given name of some person."""
propDocs["holdsAccount"]=\
"""Indicates an account held by this agent."""
propDocs["holdsAccount"]=\
"""Indicates an account held by this agent."""
propDocs["homepage"]=\
"""A homepage for some thing."""
propDocs["homepage"]=\
"""A homepage for some thing."""
propDocs["icqChatID"]=\
"""An ICQ chat ID"""
propDocs["icqChatID"]=\
"""An ICQ chat ID"""
propDocs["img"]=\
"""An image that can be used to represent some thing (ie. those depictions which are particularly representative of something, eg. one's photo on a homepage)."""
propDocs["img"]=\
"""An image that can be used to represent some thing (ie. those depictions which are particularly representative of something, eg. one's photo on a homepage)."""
propDocs["interest"]=\
"""A page about a topic of interest to this person."""
propDocs["interest"]=\
"""A page about a topic of interest to this person."""
propDocs["isPrimaryTopicOf"]=\
"""A document that this thing is the primary topic of."""
propDocs["jabberID"]=\
"""A jabber ID for something."""
propDocs["jabberID"]=\
"""A jabber ID for something."""
propDocs["knows"]=\
"""A person known by this person (indicating some level of reciprocated interaction between the parties)."""
propDocs["knows"]=\
"""A person known by this person (indicating some level of reciprocated interaction between the parties)."""
propDocs["logo"]=\
"""A logo representing some thing."""
propDocs["logo"]=\
"""A logo representing some thing."""
propDocs["made"]=\
"""Something that was made by this agent.

		Relates an agent to a manifestation he contributed to create."""
propDocs["made"]=\
"""Something that was made by this agent.

		Relates an agent to a manifestation he contributed to create."""
propDocs["maker"]=\
"""An agent that  made this thing.

		Relates a manifestation to an agent who contributed to create it.
		This property might be used for weak assertion of such a relationship. In case we want
		to attach a more concrete role (this agent performed, or was the composer, etc.), we must 
		use mo:Performer, mo:MusicalWork/mo:Composition, etc. This indeed allows to specify where a 
		particular agent took part in the actual workflow."""
propDocs["maker"]=\
"""An agent that  made this thing.

		Relates a manifestation to an agent who contributed to create it.
		This property might be used for weak assertion of such a relationship. In case we want
		to attach a more concrete role (this agent performed, or was the composer, etc.), we must 
		use mo:Performer, mo:MusicalWork/mo:Composition, etc. This indeed allows to specify where a 
		particular agent took part in the actual workflow."""
propDocs["mbox"]=\
"""A  personal mailbox, ie. an Internet mailbox associated with exactly one owner, the first owner of this mailbox. This is a 'static inverse functional property', in that  there is (across time and change) at most one individual that ever has any particular value for foaf:mbox."""
propDocs["mbox"]=\
"""A  personal mailbox, ie. an Internet mailbox associated with exactly one owner, the first owner of this mailbox. This is a 'static inverse functional property', in that  there is (across time and change) at most one individual that ever has any particular value for foaf:mbox."""
propDocs["mbox_sha1sum"]=\
"""The sha1sum of the URI of an Internet mailbox associated with exactly one owner, the  first owner of the mailbox."""
propDocs["mbox_sha1sum"]=\
"""The sha1sum of the URI of an Internet mailbox associated with exactly one owner, the  first owner of the mailbox."""
propDocs["member"]=\
"""Indicates a member of a Group
	
Indicates a member of a Group"""
propDocs["member"]=\
"""Indicates a member of a Group
	
Indicates a member of a Group"""
propDocs["membershipClass"]=\
"""Indicates the class of individuals that are a member of a Group"""
propDocs["membershipClass"]=\
"""Indicates the class of individuals that are a member of a Group"""
propDocs["msnChatID"]=\
"""An MSN chat ID"""
propDocs["msnChatID"]=\
"""An MSN chat ID"""
propDocs["myersBriggs"]=\
"""A Myers Briggs (MBTI) personality classification."""
propDocs["myersBriggs"]=\
"""A Myers Briggs (MBTI) personality classification."""
propDocs["name"]=\
"""A name for some thing."""
propDocs["name"]=\
"""A name for some thing."""
propDocs["nick"]=\
"""A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames)."""
propDocs["nick"]=\
"""A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames)."""
propDocs["openid"]=\
"""An OpenID  for an Agent."""
propDocs["openid"]=\
"""An OpenID  for an Agent."""
propDocs["page"]=\
"""A page or document about this thing."""
propDocs["page"]=\
"""A page or document about this thing."""
propDocs["pastProject"]=\
"""A project this person has previously worked on."""
propDocs["pastProject"]=\
"""A project this person has previously worked on."""
propDocs["phone"]=\
"""A phone,  specified using fully qualified tel: URI scheme (refs: http://www.w3.org/Addressing/schemes.html#tel)."""
propDocs["phone"]=\
"""A phone,  specified using fully qualified tel: URI scheme (refs: http://www.w3.org/Addressing/schemes.html#tel)."""
propDocs["plan"]=\
"""A .plan comment, in the tradition of finger and '.plan' files."""
propDocs["plan"]=\
"""A .plan comment, in the tradition of finger and '.plan' files."""
propDocs["primaryTopic"]=\
"""The primary topic of some page or document."""
propDocs["primaryTopic"]=\
"""The primary topic of some page or document."""
propDocs["primaryTopic"]=\
"""The primary topic of some page or document."""
propDocs["publications"]=\
"""A link to the publications of this person."""
propDocs["publications"]=\
"""A link to the publications of this person."""
propDocs["schoolHomepage"]=\
"""A homepage of a school attended by the person."""
propDocs["schoolHomepage"]=\
"""A homepage of a school attended by the person."""
propDocs["sha1"]=\
"""A sha1sum hash, in hex."""
propDocs["sha1"]=\
"""A sha1sum hash, in hex."""
propDocs["surname"]=\
"""The surname of some person."""
propDocs["surname"]=\
"""The surname of some person."""
propDocs["theme"]=\
"""A theme."""
propDocs["theme"]=\
"""A theme."""
propDocs["thumbnail"]=\
"""A derived thumbnail image."""
propDocs["thumbnail"]=\
"""A derived thumbnail image."""
propDocs["tipjar"]=\
"""A tipjar document for this agent, describing means for payment and reward."""
propDocs["tipjar"]=\
"""A tipjar document for this agent, describing means for payment and reward."""
propDocs["title"]=\
"""Title (Mr, Mrs, Ms, Dr. etc)"""
propDocs["title"]=\
"""Title (Mr, Mrs, Ms, Dr. etc)"""
propDocs["topic"]=\
"""A topic of some page or document."""
propDocs["topic"]=\
"""A topic of some page or document."""
propDocs["topic_interest"]=\
"""A thing of interest to this person."""
propDocs["topic_interest"]=\
"""A thing of interest to this person."""
propDocs["weblog"]=\
"""A weblog of some thing (whether person, group, company etc.)."""
propDocs["weblog"]=\
"""A weblog of some thing (whether person, group, company etc.)."""
propDocs["workInfoHomepage"]=\
"""A work info homepage of some person; a page about their work for some organization."""
propDocs["workInfoHomepage"]=\
"""A work info homepage of some person; a page about their work for some organization."""
propDocs["workplaceHomepage"]=\
"""A workplace homepage of some person; the homepage of an organization they work for."""
propDocs["workplaceHomepage"]=\
"""A workplace homepage of some person; the homepage of an organization they work for."""
propDocs["yahooChatID"]=\
"""A Yahoo chat ID"""
propDocs["yahooChatID"]=\
"""A Yahoo chat ID"""
propDocs["assurance"]=""
propDocs["src_assurance"]=""




# ========================  Class Definitions  ====================== 

class owl___Thing(object):
	"""
	owl:Thing
	"""
	def __init__(self,URI=None):
		self._initialised = False
		self.shortname = "Thing"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["amazon_asin"] = PropertySet("amazon_asin","http://purl.org/ontology/mo/amazon_asin", foaf___Document, False)
		self._props["biography"] = PropertySet("biography","http://purl.org/ontology/mo/biography", foaf___Document, False)
		self._props["discography"] = PropertySet("discography","http://purl.org/ontology/mo/discography", foaf___Document, False)
		self._props["discogs"] = PropertySet("discogs","http://purl.org/ontology/mo/discogs", foaf___Document, False)
		self._props["download"] = PropertySet("download","http://purl.org/ontology/mo/download", foaf___Document, False)
		self._props["event_homepage"] = PropertySet("event_homepage","http://purl.org/ontology/mo/event_homepage", foaf___Document, False)
		self._props["fanpage"] = PropertySet("fanpage","http://purl.org/ontology/mo/fanpage", foaf___Document, False)
		self._props["free_download"] = PropertySet("free_download","http://purl.org/ontology/mo/free_download", foaf___Document, False)
		self._props["image"] = PropertySet("image","http://purl.org/ontology/mo/image", (foaf___Image,rdfs___Resource), False)
		self._props["imdb"] = PropertySet("imdb","http://purl.org/ontology/mo/imdb", foaf___Document, False)
		self._props["licence"] = PropertySet("licence","http://purl.org/ontology/mo/licence", foaf___Document, False)
		self._props["mailorder"] = PropertySet("mailorder","http://purl.org/ontology/mo/mailorder", foaf___Document, False)
		self._props["musicbrainz"] = PropertySet("musicbrainz","http://purl.org/ontology/mo/musicbrainz", foaf___Document, False)
		self._props["musicmoz"] = PropertySet("musicmoz","http://purl.org/ontology/mo/musicmoz", foaf___Document, False)
		self._props["myspace"] = PropertySet("myspace","http://purl.org/ontology/mo/myspace", foaf___Document, False)
		self._props["olga"] = PropertySet("olga","http://purl.org/ontology/mo/olga", foaf___Document, False)
		self._props["onlinecommunity"] = PropertySet("onlinecommunity","http://purl.org/ontology/mo/onlinecommunity", foaf___Document, False)
		self._props["paid_download"] = PropertySet("paid_download","http://purl.org/ontology/mo/paid_download", foaf___Document, False)
		self._props["preview_download"] = PropertySet("preview_download","http://purl.org/ontology/mo/preview_download", foaf___Document, False)
		self._props["review"] = PropertySet("review","http://purl.org/ontology/mo/review", foaf___Document, False)
		self._props["wikipedia"] = PropertySet("wikipedia","http://purl.org/ontology/mo/wikipedia", foaf___Document, False)
		self._props["differentFrom"] = PropertySet("differentFrom","http://www.w3.org/2002/07/owl#differentFrom", owl___Thing, False)
		self._props["sameAs"] = PropertySet("sameAs","http://www.w3.org/2002/07/owl#sameAs", owl___Thing, False)
		self._props["depiction"] = PropertySet("depiction","http://xmlns.com/foaf/0.1/depiction", foaf___Image, False)
		self._props["fundedBy"] = PropertySet("fundedBy","http://xmlns.com/foaf/0.1/fundedBy", owl___Thing, False)
		self._props["homepage"] = PropertySet("homepage","http://xmlns.com/foaf/0.1/homepage", foaf___Document, False)
		self._props["img"] = PropertySet("img","http://xmlns.com/foaf/0.1/img", foaf___Image, False)
		self._props["isPrimaryTopicOf"] = PropertySet("isPrimaryTopicOf","http://xmlns.com/foaf/0.1/isPrimaryTopicOf", foaf___Document, False)
		self._props["logo"] = PropertySet("logo","http://xmlns.com/foaf/0.1/logo", owl___Thing, False)
		self._props["made"] = PropertySet("made","http://xmlns.com/foaf/0.1/made", (mo___Track,owl___Thing,mo___MusicalManifestation,mo___Record), False)
		self._props["maker"] = PropertySet("maker","http://xmlns.com/foaf/0.1/maker", foaf___Agent, False)
		self._props["name"] = PropertySet("name","http://xmlns.com/foaf/0.1/name", None, True)
		self._props["openid"] = PropertySet("openid","http://xmlns.com/foaf/0.1/openid", foaf___Document, False)
		self._props["page"] = PropertySet("page","http://xmlns.com/foaf/0.1/page", foaf___Document, False)
		self._props["theme"] = PropertySet("theme","http://xmlns.com/foaf/0.1/theme", owl___Thing, False)
		self._props["tipjar"] = PropertySet("tipjar","http://xmlns.com/foaf/0.1/tipjar", foaf___Document, False)
		self._props["weblog"] = PropertySet("weblog","http://xmlns.com/foaf/0.1/weblog", foaf___Document, False)
		self._initialised = True
	classURI = "http://www.w3.org/2002/07/owl#Thing"


	# Python class properties to wrap the PropertySet objects
	amazon_asin = property(fget=lambda x: x._props["amazon_asin"].get(), fset=lambda x,y : x._props["amazon_asin"].set(y), fdel=None, doc=propDocs["amazon_asin"])
	biography = property(fget=lambda x: x._props["biography"].get(), fset=lambda x,y : x._props["biography"].set(y), fdel=None, doc=propDocs["biography"])
	discography = property(fget=lambda x: x._props["discography"].get(), fset=lambda x,y : x._props["discography"].set(y), fdel=None, doc=propDocs["discography"])
	discogs = property(fget=lambda x: x._props["discogs"].get(), fset=lambda x,y : x._props["discogs"].set(y), fdel=None, doc=propDocs["discogs"])
	download = property(fget=lambda x: x._props["download"].get(), fset=lambda x,y : x._props["download"].set(y), fdel=None, doc=propDocs["download"])
	event_homepage = property(fget=lambda x: x._props["event_homepage"].get(), fset=lambda x,y : x._props["event_homepage"].set(y), fdel=None, doc=propDocs["event_homepage"])
	fanpage = property(fget=lambda x: x._props["fanpage"].get(), fset=lambda x,y : x._props["fanpage"].set(y), fdel=None, doc=propDocs["fanpage"])
	free_download = property(fget=lambda x: x._props["free_download"].get(), fset=lambda x,y : x._props["free_download"].set(y), fdel=None, doc=propDocs["free_download"])
	image = property(fget=lambda x: x._props["image"].get(), fset=lambda x,y : x._props["image"].set(y), fdel=None, doc=propDocs["image"])
	imdb = property(fget=lambda x: x._props["imdb"].get(), fset=lambda x,y : x._props["imdb"].set(y), fdel=None, doc=propDocs["imdb"])
	licence = property(fget=lambda x: x._props["licence"].get(), fset=lambda x,y : x._props["licence"].set(y), fdel=None, doc=propDocs["licence"])
	mailorder = property(fget=lambda x: x._props["mailorder"].get(), fset=lambda x,y : x._props["mailorder"].set(y), fdel=None, doc=propDocs["mailorder"])
	musicbrainz = property(fget=lambda x: x._props["musicbrainz"].get(), fset=lambda x,y : x._props["musicbrainz"].set(y), fdel=None, doc=propDocs["musicbrainz"])
	musicmoz = property(fget=lambda x: x._props["musicmoz"].get(), fset=lambda x,y : x._props["musicmoz"].set(y), fdel=None, doc=propDocs["musicmoz"])
	myspace = property(fget=lambda x: x._props["myspace"].get(), fset=lambda x,y : x._props["myspace"].set(y), fdel=None, doc=propDocs["myspace"])
	olga = property(fget=lambda x: x._props["olga"].get(), fset=lambda x,y : x._props["olga"].set(y), fdel=None, doc=propDocs["olga"])
	onlinecommunity = property(fget=lambda x: x._props["onlinecommunity"].get(), fset=lambda x,y : x._props["onlinecommunity"].set(y), fdel=None, doc=propDocs["onlinecommunity"])
	paid_download = property(fget=lambda x: x._props["paid_download"].get(), fset=lambda x,y : x._props["paid_download"].set(y), fdel=None, doc=propDocs["paid_download"])
	preview_download = property(fget=lambda x: x._props["preview_download"].get(), fset=lambda x,y : x._props["preview_download"].set(y), fdel=None, doc=propDocs["preview_download"])
	review = property(fget=lambda x: x._props["review"].get(), fset=lambda x,y : x._props["review"].set(y), fdel=None, doc=propDocs["review"])
	wikipedia = property(fget=lambda x: x._props["wikipedia"].get(), fset=lambda x,y : x._props["wikipedia"].set(y), fdel=None, doc=propDocs["wikipedia"])
	differentFrom = property(fget=lambda x: x._props["differentFrom"].get(), fset=lambda x,y : x._props["differentFrom"].set(y), fdel=None, doc=propDocs["differentFrom"])
	sameAs = property(fget=lambda x: x._props["sameAs"].get(), fset=lambda x,y : x._props["sameAs"].set(y), fdel=None, doc=propDocs["sameAs"])
	depiction = property(fget=lambda x: x._props["depiction"].get(), fset=lambda x,y : x._props["depiction"].set(y), fdel=None, doc=propDocs["depiction"])
	fundedBy = property(fget=lambda x: x._props["fundedBy"].get(), fset=lambda x,y : x._props["fundedBy"].set(y), fdel=None, doc=propDocs["fundedBy"])
	homepage = property(fget=lambda x: x._props["homepage"].get(), fset=lambda x,y : x._props["homepage"].set(y), fdel=None, doc=propDocs["homepage"])
	img = property(fget=lambda x: x._props["img"].get(), fset=lambda x,y : x._props["img"].set(y), fdel=None, doc=propDocs["img"])
	isPrimaryTopicOf = property(fget=lambda x: x._props["isPrimaryTopicOf"].get(), fset=lambda x,y : x._props["isPrimaryTopicOf"].set(y), fdel=None, doc=propDocs["isPrimaryTopicOf"])
	logo = property(fget=lambda x: x._props["logo"].get(), fset=lambda x,y : x._props["logo"].set(y), fdel=None, doc=propDocs["logo"])
	made = property(fget=lambda x: x._props["made"].get(), fset=lambda x,y : x._props["made"].set(y), fdel=None, doc=propDocs["made"])
	maker = property(fget=lambda x: x._props["maker"].get(), fset=lambda x,y : x._props["maker"].set(y), fdel=None, doc=propDocs["maker"])
	name = property(fget=lambda x: x._props["name"].get(), fset=lambda x,y : x._props["name"].set(y), fdel=None, doc=propDocs["name"])
	openid = property(fget=lambda x: x._props["openid"].get(), fset=lambda x,y : x._props["openid"].set(y), fdel=None, doc=propDocs["openid"])
	page = property(fget=lambda x: x._props["page"].get(), fset=lambda x,y : x._props["page"].set(y), fdel=None, doc=propDocs["page"])
	theme = property(fget=lambda x: x._props["theme"].get(), fset=lambda x,y : x._props["theme"].set(y), fdel=None, doc=propDocs["theme"])
	tipjar = property(fget=lambda x: x._props["tipjar"].get(), fset=lambda x,y : x._props["tipjar"].set(y), fdel=None, doc=propDocs["tipjar"])
	weblog = property(fget=lambda x: x._props["weblog"].get(), fset=lambda x,y : x._props["weblog"].set(y), fdel=None, doc=propDocs["weblog"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___OnlineAccount(owl___Thing):
	"""
	foaf:OnlineAccount
	An online account.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owl___Thing.__init__(self)
		self._initialised = False
		self.shortname = "OnlineAccount"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["accountName"] = PropertySet("accountName","http://xmlns.com/foaf/0.1/accountName", None, True)
		self._props["accountServiceHomepage"] = PropertySet("accountServiceHomepage","http://xmlns.com/foaf/0.1/accountServiceHomepage", foaf___Document, False)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/OnlineAccount"


	# Python class properties to wrap the PropertySet objects
	accountName = property(fget=lambda x: x._props["accountName"].get(), fset=lambda x,y : x._props["accountName"].set(y), fdel=None, doc=propDocs["accountName"])
	accountServiceHomepage = property(fget=lambda x: x._props["accountServiceHomepage"].get(), fset=lambda x,y : x._props["accountServiceHomepage"].set(y), fdel=None, doc=propDocs["accountServiceHomepage"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___OnlineEcommerceAccount(foaf___OnlineAccount):
	"""
	foaf:OnlineEcommerceAccount
	An online e-commerce account.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___OnlineAccount.__init__(self)
		self._initialised = False
		self.shortname = "OnlineEcommerceAccount"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/OnlineEcommerceAccount"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class rdfs___Resource(owl___Thing):
	"""
	rdfs:Resource
	"""
	def __init__(self,URI=None):
		# Initialise parents
		owl___Thing.__init__(self)
		self._initialised = False
		self.shortname = "Resource"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["isFactorOf"] = PropertySet("isFactorOf","http://purl.org/NET/c4dm/event.owl#isFactorOf", event___Event, False)
		self._props["producedIn"] = PropertySet("producedIn","http://purl.org/NET/c4dm/event.owl#producedIn", event___Event, False)
		self._props["creator"] = PropertySet("creator","http://purl.org/dc/elements/1.1/creator", foaf___Agent, False)
		self._props["description"] = PropertySet("description","http://purl.org/dc/elements/1.1/description", None, True)
		self._props["title"] = PropertySet("title","http://purl.org/dc/elements/1.1/title", None, True)
		self._props["arranged_in"] = PropertySet("arranged_in","http://purl.org/ontology/mo/arranged_in", (mo___Arrangement,event___Event), False)
		self._props["composed_in"] = PropertySet("composed_in","http://purl.org/ontology/mo/composed_in", (mo___Composition,event___Event), False)
		self._props["performed_in"] = PropertySet("performed_in","http://purl.org/ontology/mo/performed_in", (mo___Performance,event___Event), False)
		self._props["recorded_in"] = PropertySet("recorded_in","http://purl.org/ontology/mo/recorded_in", (mo___Recording,event___Event), False)
		self._props["label"] = PropertySet("label","http://www.w3.org/2000/01/rdf-schema#label", None, True)
		self._props["name"] = PropertySet("name","http://xmlns.com/foaf/0.1/name", None, True)
		self._initialised = True
	classURI = "http://www.w3.org/2000/01/rdf-schema#Resource"


	# Python class properties to wrap the PropertySet objects
	isFactorOf = property(fget=lambda x: x._props["isFactorOf"].get(), fset=lambda x,y : x._props["isFactorOf"].set(y), fdel=None, doc=propDocs["isFactorOf"])
	producedIn = property(fget=lambda x: x._props["producedIn"].get(), fset=lambda x,y : x._props["producedIn"].set(y), fdel=None, doc=propDocs["producedIn"])
	creator = property(fget=lambda x: x._props["creator"].get(), fset=lambda x,y : x._props["creator"].set(y), fdel=None, doc=propDocs["creator"])
	description = property(fget=lambda x: x._props["description"].get(), fset=lambda x,y : x._props["description"].set(y), fdel=None, doc=propDocs["description"])
	title = property(fget=lambda x: x._props["title"].get(), fset=lambda x,y : x._props["title"].set(y), fdel=None, doc=propDocs["title"])
	arranged_in = property(fget=lambda x: x._props["arranged_in"].get(), fset=lambda x,y : x._props["arranged_in"].set(y), fdel=None, doc=propDocs["arranged_in"])
	composed_in = property(fget=lambda x: x._props["composed_in"].get(), fset=lambda x,y : x._props["composed_in"].set(y), fdel=None, doc=propDocs["composed_in"])
	performed_in = property(fget=lambda x: x._props["performed_in"].get(), fset=lambda x,y : x._props["performed_in"].set(y), fdel=None, doc=propDocs["performed_in"])
	recorded_in = property(fget=lambda x: x._props["recorded_in"].get(), fset=lambda x,y : x._props["recorded_in"].set(y), fdel=None, doc=propDocs["recorded_in"])
	label = property(fget=lambda x: x._props["label"].get(), fset=lambda x,y : x._props["label"].set(y), fdel=None, doc=propDocs["label"])
	name = property(fget=lambda x: x._props["name"].get(), fset=lambda x,y : x._props["name"].set(y), fdel=None, doc=propDocs["name"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class geo___SpatialThing(rdfs___Resource):
	"""
	geo:SpatialThing
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "SpatialThing"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["based_near"] = PropertySet("based_near","http://xmlns.com/foaf/0.1/based_near", geo___SpatialThing, False)
		self._initialised = True
	classURI = "http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing"


	# Python class properties to wrap the PropertySet objects
	based_near = property(fget=lambda x: x._props["based_near"].get(), fset=lambda x,y : x._props["based_near"].set(y), fdel=None, doc=propDocs["based_near"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___DayOfWeek(rdfs___Resource):
	"""
	time:DayOfWeek
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DayOfWeek"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#DayOfWeek"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___TemporalEntity(rdfs___Resource):
	"""
	time:TemporalEntity
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TemporalEntity"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["after"] = PropertySet("after","http://www.w3.org/2006/time#after", None, False)
		self._props["before"] = PropertySet("before","http://www.w3.org/2006/time#before", time___TemporalEntity, False)
		self._props["hasBeginning"] = PropertySet("hasBeginning","http://www.w3.org/2006/time#hasBeginning", time___Instant, False)
		self._props["hasDurationDescription"] = PropertySet("hasDurationDescription","http://www.w3.org/2006/time#hasDurationDescription", time___DurationDescription, False)
		self._props["hasEnd"] = PropertySet("hasEnd","http://www.w3.org/2006/time#hasEnd", time___Instant, False)
		self._props["intervalBefore"] = PropertySet("intervalBefore","http://www.w3.org/2006/time#intervalBefore", (time___ProperInterval,time___TemporalEntity,time___Interval), False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#TemporalEntity"


	# Python class properties to wrap the PropertySet objects
	after = property(fget=lambda x: x._props["after"].get(), fset=lambda x,y : x._props["after"].set(y), fdel=None, doc=propDocs["after"])
	before = property(fget=lambda x: x._props["before"].get(), fset=lambda x,y : x._props["before"].set(y), fdel=None, doc=propDocs["before"])
	hasBeginning = property(fget=lambda x: x._props["hasBeginning"].get(), fset=lambda x,y : x._props["hasBeginning"].set(y), fdel=None, doc=propDocs["hasBeginning"])
	hasDurationDescription = property(fget=lambda x: x._props["hasDurationDescription"].get(), fset=lambda x,y : x._props["hasDurationDescription"].set(y), fdel=None, doc=propDocs["hasDurationDescription"])
	hasEnd = property(fget=lambda x: x._props["hasEnd"].get(), fset=lambda x,y : x._props["hasEnd"].set(y), fdel=None, doc=propDocs["hasEnd"])
	intervalBefore = property(fget=lambda x: x._props["intervalBefore"].get(), fset=lambda x,y : x._props["intervalBefore"].set(y), fdel=None, doc=propDocs["intervalBefore"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class tzont___TimeZone(rdfs___Resource):
	"""
	tzont:TimeZone
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TimeZone"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2006/timezone#TimeZone"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Document(rdfs___Resource):
	"""
	foaf:Document
	A document.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Document"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["primaryTopic"] = PropertySet("primaryTopic","http://xmlns.com/foaf/0.1/primaryTopic", owl___Thing, False)
		self._props["sha1"] = PropertySet("sha1","http://xmlns.com/foaf/0.1/sha1", None, False)
		self._props["topic"] = PropertySet("topic","http://xmlns.com/foaf/0.1/topic", owl___Thing, False)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Document"


	# Python class properties to wrap the PropertySet objects
	primaryTopic = property(fget=lambda x: x._props["primaryTopic"].get(), fset=lambda x,y : x._props["primaryTopic"].set(y), fdel=None, doc=propDocs["primaryTopic"])
	sha1 = property(fget=lambda x: x._props["sha1"].get(), fset=lambda x,y : x._props["sha1"].set(y), fdel=None, doc=propDocs["sha1"])
	topic = property(fget=lambda x: x._props["topic"].get(), fset=lambda x,y : x._props["topic"].set(y), fdel=None, doc=propDocs["topic"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Image(rdfs___Resource):
	"""
	foaf:Image
	An image.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Image"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["depicts"] = PropertySet("depicts","http://xmlns.com/foaf/0.1/depicts", owl___Thing, False)
		self._props["thumbnail"] = PropertySet("thumbnail","http://xmlns.com/foaf/0.1/thumbnail", foaf___Image, False)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Image"


	# Python class properties to wrap the PropertySet objects
	depicts = property(fget=lambda x: x._props["depicts"].get(), fset=lambda x,y : x._props["depicts"].set(y), fdel=None, doc=propDocs["depicts"])
	thumbnail = property(fget=lambda x: x._props["thumbnail"].get(), fset=lambda x,y : x._props["thumbnail"].set(y), fdel=None, doc=propDocs["thumbnail"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___OnlineGamingAccount(foaf___OnlineAccount):
	"""
	foaf:OnlineGamingAccount
	An online gaming account.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___OnlineAccount.__init__(self)
		self._initialised = False
		self.shortname = "OnlineGamingAccount"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/OnlineGamingAccount"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___PersonalProfileDocument(foaf___Document):
	"""
	foaf:PersonalProfileDocument
	A personal profile RDF document.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Document.__init__(self)
		self._initialised = False
		self.shortname = "PersonalProfileDocument"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/PersonalProfileDocument"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class event___Event(rdfs___Resource):
	"""
	event:Event
	 
		An event: a way of arbitrary classifying a space/time region.
		An event has agents (active entities contributing to the event -- a performer, a composer, an engineer, ...),
		factors (passive entities contributing to the event -- flute, score, ...),
		and products (things produced by the event -- sound, signal, score, ...). For
		example, we may describe as Events: performances, composition events, recordings, arrangements,
		creation of a musical group, separation of a musical group,
		but also sounds, signals, notes (in a score)...
	
	
		An arbitrary classification of a space/time region, by a 
		cognitive agent. An event may have actively participating agents,
		passive factors, products, and a location in space/time.
		
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Event"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasAgent"] = PropertySet("hasAgent","http://purl.org/NET/c4dm/event.owl#hasAgent", foaf___Agent, False)
		self._props["hasFactor"] = PropertySet("hasFactor","http://purl.org/NET/c4dm/event.owl#hasFactor", rdfs___Resource, False)
		self._props["hasLiteralFactor"] = PropertySet("hasLiteralFactor","http://purl.org/NET/c4dm/event.owl#hasLiteralFactor", None, False)
		self._props["hasProduct"] = PropertySet("hasProduct","http://purl.org/NET/c4dm/event.owl#hasProduct", rdfs___Resource, False)
		self._props["hasSubEvent"] = PropertySet("hasSubEvent","http://purl.org/NET/c4dm/event.owl#hasSubEvent", event___Event, False)
		self._props["place"] = PropertySet("place","http://purl.org/NET/c4dm/event.owl#place", geo___SpatialThing, False)
		self._props["time"] = PropertySet("time","http://purl.org/NET/c4dm/event.owl#time", time___TemporalEntity, False)
		self._props["arrangement_of"] = PropertySet("arrangement_of","http://purl.org/ontology/mo/arrangement_of", (mo___MusicalWork,rdfs___Resource), False)
		self._props["composer"] = PropertySet("composer","http://purl.org/ontology/mo/composer", foaf___Agent, False)
		self._props["conductor"] = PropertySet("conductor","http://purl.org/ontology/mo/conductor", foaf___Agent, False)
		self._props["engineer"] = PropertySet("engineer","http://purl.org/ontology/mo/engineer", foaf___Agent, False)
		self._props["event_homepage"] = PropertySet("event_homepage","http://purl.org/ontology/mo/event_homepage", foaf___Document, False)
		self._props["genre"] = PropertySet("genre","http://purl.org/ontology/mo/genre", (mo___Genre,rdfs___Resource), False)
		self._props["instrument"] = PropertySet("instrument","http://purl.org/ontology/mo/instrument", (rdfs___Resource,mo___Instrument), False)
		self._props["key"] = PropertySet("key","http://purl.org/ontology/mo/key", (rdfs___Resource,key___Key), False)
		self._props["listener"] = PropertySet("listener","http://purl.org/ontology/mo/listener", foaf___Agent, False)
		self._props["performance_of"] = PropertySet("performance_of","http://purl.org/ontology/mo/performance_of", (mo___MusicalWork,rdfs___Resource,mo___Score), False)
		self._props["performer"] = PropertySet("performer","http://purl.org/ontology/mo/performer", foaf___Agent, False)
		self._props["produced_score"] = PropertySet("produced_score","http://purl.org/ontology/mo/produced_score", (rdfs___Resource,mo___Score), False)
		self._props["produced_signal"] = PropertySet("produced_signal","http://purl.org/ontology/mo/produced_signal", (mo___Signal,rdfs___Resource), False)
		self._props["produced_sound"] = PropertySet("produced_sound","http://purl.org/ontology/mo/produced_sound", (rdfs___Resource,mo___Sound), False)
		self._props["produced_work"] = PropertySet("produced_work","http://purl.org/ontology/mo/produced_work", (mo___MusicalWork,rdfs___Resource), False)
		self._props["recording_of"] = PropertySet("recording_of","http://purl.org/ontology/mo/recording_of", (rdfs___Resource,mo___Sound), False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/event.owl#Event"


	# Python class properties to wrap the PropertySet objects
	hasAgent = property(fget=lambda x: x._props["hasAgent"].get(), fset=lambda x,y : x._props["hasAgent"].set(y), fdel=None, doc=propDocs["hasAgent"])
	hasFactor = property(fget=lambda x: x._props["hasFactor"].get(), fset=lambda x,y : x._props["hasFactor"].set(y), fdel=None, doc=propDocs["hasFactor"])
	hasLiteralFactor = property(fget=lambda x: x._props["hasLiteralFactor"].get(), fset=lambda x,y : x._props["hasLiteralFactor"].set(y), fdel=None, doc=propDocs["hasLiteralFactor"])
	hasProduct = property(fget=lambda x: x._props["hasProduct"].get(), fset=lambda x,y : x._props["hasProduct"].set(y), fdel=None, doc=propDocs["hasProduct"])
	hasSubEvent = property(fget=lambda x: x._props["hasSubEvent"].get(), fset=lambda x,y : x._props["hasSubEvent"].set(y), fdel=None, doc=propDocs["hasSubEvent"])
	place = property(fget=lambda x: x._props["place"].get(), fset=lambda x,y : x._props["place"].set(y), fdel=None, doc=propDocs["place"])
	time = property(fget=lambda x: x._props["time"].get(), fset=lambda x,y : x._props["time"].set(y), fdel=None, doc=propDocs["time"])
	arrangement_of = property(fget=lambda x: x._props["arrangement_of"].get(), fset=lambda x,y : x._props["arrangement_of"].set(y), fdel=None, doc=propDocs["arrangement_of"])
	composer = property(fget=lambda x: x._props["composer"].get(), fset=lambda x,y : x._props["composer"].set(y), fdel=None, doc=propDocs["composer"])
	conductor = property(fget=lambda x: x._props["conductor"].get(), fset=lambda x,y : x._props["conductor"].set(y), fdel=None, doc=propDocs["conductor"])
	engineer = property(fget=lambda x: x._props["engineer"].get(), fset=lambda x,y : x._props["engineer"].set(y), fdel=None, doc=propDocs["engineer"])
	event_homepage = property(fget=lambda x: x._props["event_homepage"].get(), fset=lambda x,y : x._props["event_homepage"].set(y), fdel=None, doc=propDocs["event_homepage"])
	genre = property(fget=lambda x: x._props["genre"].get(), fset=lambda x,y : x._props["genre"].set(y), fdel=None, doc=propDocs["genre"])
	instrument = property(fget=lambda x: x._props["instrument"].get(), fset=lambda x,y : x._props["instrument"].set(y), fdel=None, doc=propDocs["instrument"])
	key = property(fget=lambda x: x._props["key"].get(), fset=lambda x,y : x._props["key"].set(y), fdel=None, doc=propDocs["key"])
	listener = property(fget=lambda x: x._props["listener"].get(), fset=lambda x,y : x._props["listener"].set(y), fdel=None, doc=propDocs["listener"])
	performance_of = property(fget=lambda x: x._props["performance_of"].get(), fset=lambda x,y : x._props["performance_of"].set(y), fdel=None, doc=propDocs["performance_of"])
	performer = property(fget=lambda x: x._props["performer"].get(), fset=lambda x,y : x._props["performer"].set(y), fdel=None, doc=propDocs["performer"])
	produced_score = property(fget=lambda x: x._props["produced_score"].get(), fset=lambda x,y : x._props["produced_score"].set(y), fdel=None, doc=propDocs["produced_score"])
	produced_signal = property(fget=lambda x: x._props["produced_signal"].get(), fset=lambda x,y : x._props["produced_signal"].set(y), fdel=None, doc=propDocs["produced_signal"])
	produced_sound = property(fget=lambda x: x._props["produced_sound"].get(), fset=lambda x,y : x._props["produced_sound"].set(y), fdel=None, doc=propDocs["produced_sound"])
	produced_work = property(fget=lambda x: x._props["produced_work"].get(), fset=lambda x,y : x._props["produced_work"].set(y), fdel=None, doc=propDocs["produced_work"])
	recording_of = property(fget=lambda x: x._props["recording_of"].get(), fset=lambda x,y : x._props["recording_of"].set(y), fdel=None, doc=propDocs["recording_of"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class event___Product(rdfs___Resource):
	"""
	event:Product
	
		Everything produced by an event
		
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Product"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/event.owl#Product"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class key___Note(rdfs___Resource):
	"""
	key:Note
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Note"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/keys.owl#Note"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___DiscreteInstant(rdfs___Resource):
	"""
	timeline:DiscreteInstant
	An instant defined on a discrete timeline
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DiscreteInstant"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#DiscreteInstant"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___Instant(time___TemporalEntity):
	"""
	timeline:Instant
	An instant (same as in OWL-Time)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		time___TemporalEntity.__init__(self)
		self._initialised = False
		self.shortname = "Instant"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["at"] = PropertySet("at","http://purl.org/NET/c4dm/timeline.owl#at", None, False)
		self._props["atDate"] = PropertySet("atDate","http://purl.org/NET/c4dm/timeline.owl#atDate", str, False)
		self._props["atDateTime"] = PropertySet("atDateTime","http://purl.org/NET/c4dm/timeline.owl#atDateTime", str, True)
		self._props["atDuration"] = PropertySet("atDuration","http://purl.org/NET/c4dm/timeline.owl#atDuration", str, True)
		self._props["atInt"] = PropertySet("atInt","http://purl.org/NET/c4dm/timeline.owl#atInt", int, False)
		self._props["atReal"] = PropertySet("atReal","http://purl.org/NET/c4dm/timeline.owl#atReal", float, False)
		self._props["atYear"] = PropertySet("atYear","http://purl.org/NET/c4dm/timeline.owl#atYear", int, False)
		self._props["atYearMonth"] = PropertySet("atYearMonth","http://purl.org/NET/c4dm/timeline.owl#atYearMonth", str, False)
		self._props["onTimeLine"] = PropertySet("onTimeLine","http://purl.org/NET/c4dm/timeline.owl#onTimeLine", timeline___TimeLine, False)
		self._props["inDateTime"] = PropertySet("inDateTime","http://www.w3.org/2006/time#inDateTime", time___DateTimeDescription, False)
		self._props["inXSDDateTime"] = PropertySet("inXSDDateTime","http://www.w3.org/2006/time#inXSDDateTime", str, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#Instant"


	# Python class properties to wrap the PropertySet objects
	at = property(fget=lambda x: x._props["at"].get(), fset=lambda x,y : x._props["at"].set(y), fdel=None, doc=propDocs["at"])
	atDate = property(fget=lambda x: x._props["atDate"].get(), fset=lambda x,y : x._props["atDate"].set(y), fdel=None, doc=propDocs["atDate"])
	atDateTime = property(fget=lambda x: x._props["atDateTime"].get(), fset=lambda x,y : x._props["atDateTime"].set(y), fdel=None, doc=propDocs["atDateTime"])
	atDuration = property(fget=lambda x: x._props["atDuration"].get(), fset=lambda x,y : x._props["atDuration"].set(y), fdel=None, doc=propDocs["atDuration"])
	atInt = property(fget=lambda x: x._props["atInt"].get(), fset=lambda x,y : x._props["atInt"].set(y), fdel=None, doc=propDocs["atInt"])
	atReal = property(fget=lambda x: x._props["atReal"].get(), fset=lambda x,y : x._props["atReal"].set(y), fdel=None, doc=propDocs["atReal"])
	atYear = property(fget=lambda x: x._props["atYear"].get(), fset=lambda x,y : x._props["atYear"].set(y), fdel=None, doc=propDocs["atYear"])
	atYearMonth = property(fget=lambda x: x._props["atYearMonth"].get(), fset=lambda x,y : x._props["atYearMonth"].set(y), fdel=None, doc=propDocs["atYearMonth"])
	onTimeLine = property(fget=lambda x: x._props["onTimeLine"].get(), fset=lambda x,y : x._props["onTimeLine"].set(y), fdel=None, doc=propDocs["onTimeLine"])
	inDateTime = property(fget=lambda x: x._props["inDateTime"].get(), fset=lambda x,y : x._props["inDateTime"].set(y), fdel=None, doc=propDocs["inDateTime"])
	inXSDDateTime = property(fget=lambda x: x._props["inXSDDateTime"].get(), fset=lambda x,y : x._props["inXSDDateTime"].set(y), fdel=None, doc=propDocs["inXSDDateTime"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___RelativeInstant(rdfs___Resource):
	"""
	timeline:RelativeInstant
	An instant defined on a relative timeline
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "RelativeInstant"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#RelativeInstant"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___TimeLine(rdfs___Resource):
	"""
	timeline:TimeLine
	 
		A time line -- a coherent "backbone" for addressing points and intervals.
		We can consider the timeline backing an audio/video signal, the one
		corresponding to the "physical" time, or even the one backing a score.
		Here, we consider that the timeline is *also* its coordinate system, for
		simplification purposes. In the DL version of the timeline ontology,
		coordinate systems are defined through restrictions on the way to 
		address time points/intervals on a timeline.
	
	Represents a linear and coherent piece of time -- can be either abstract (such as the one behind a score) or concrete (such as the universal time line).
Two timelines can be mapped using timeline maps.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#TimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___UTInstant(rdfs___Resource):
	"""
	timeline:UTInstant
	This concept expresses that an instant defined on the universal timeline must be associated to a dateTime value
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "UTInstant"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#UTInstant"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class chord___Chord(rdfs___Resource):
	"""
	chord:Chord
	Two or more notes played together.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Chord"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["base_chord"] = PropertySet("base_chord","http://purl.org/ontology/chord/base_chord", chord___Chord, False)
		self._props["bass"] = PropertySet("bass","http://purl.org/ontology/chord/bass", chord___Degree, False)
		self._props["interval"] = PropertySet("interval","http://purl.org/ontology/chord/interval", chord___Interval, False)
		self._props["root"] = PropertySet("root","http://purl.org/ontology/chord/root", chord___Note, False)
		self._props["without_interval"] = PropertySet("without_interval","http://purl.org/ontology/chord/without_interval", chord___ScaleInterval, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/chord/Chord"


	# Python class properties to wrap the PropertySet objects
	base_chord = property(fget=lambda x: x._props["base_chord"].get(), fset=lambda x,y : x._props["base_chord"].set(y), fdel=None, doc=propDocs["base_chord"])
	bass = property(fget=lambda x: x._props["bass"].get(), fset=lambda x,y : x._props["bass"].set(y), fdel=None, doc=propDocs["bass"])
	interval = property(fget=lambda x: x._props["interval"].get(), fset=lambda x,y : x._props["interval"].set(y), fdel=None, doc=propDocs["interval"])
	root = property(fget=lambda x: x._props["root"].get(), fset=lambda x,y : x._props["root"].set(y), fdel=None, doc=propDocs["root"])
	without_interval = property(fget=lambda x: x._props["without_interval"].get(), fset=lambda x,y : x._props["without_interval"].set(y), fdel=None, doc=propDocs["without_interval"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class chord___Degree(rdfs___Resource):
	"""
	chord:Degree
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Degree"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["modifier"] = PropertySet("modifier","http://purl.org/ontology/chord/modifier", chord___Modifier, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/chord/Degree"


	# Python class properties to wrap the PropertySet objects
	modifier = property(fget=lambda x: x._props["modifier"].get(), fset=lambda x,y : x._props["modifier"].set(y), fdel=None, doc=propDocs["modifier"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class chord___Modifier(rdfs___Resource):
	"""
	chord:Modifier
	A modifier applied to a note to change its pitch.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Modifier"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/chord/Modifier"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class chord___Note(rdfs___Resource):
	"""
	chord:Note
	FIXME
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Note"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["modifier"] = PropertySet("modifier","http://purl.org/ontology/chord/modifier", chord___Modifier, False)
		self._props["natural"] = PropertySet("natural","http://purl.org/ontology/chord/natural", chord___Natural, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/chord/Note"


	# Python class properties to wrap the PropertySet objects
	modifier = property(fget=lambda x: x._props["modifier"].get(), fset=lambda x,y : x._props["modifier"].set(y), fdel=None, doc=propDocs["modifier"])
	natural = property(fget=lambda x: x._props["natural"].get(), fset=lambda x,y : x._props["natural"].set(y), fdel=None, doc=propDocs["natural"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Arrangement(event___Event):
	"""
	mo:Arrangement
	
		An arrangement event.
		Takes as agent the arranger, and produces a score (informational object, not the actually published score).
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		event___Event.__init__(self)
		self._initialised = False
		self.shortname = "Arrangement"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["arrangement_of"] = PropertySet("arrangement_of","http://purl.org/ontology/mo/arrangement_of", (mo___MusicalWork,rdfs___Resource), False)
		self._props["genre"] = PropertySet("genre","http://purl.org/ontology/mo/genre", (mo___Genre,rdfs___Resource), False)
		self._props["produced_score"] = PropertySet("produced_score","http://purl.org/ontology/mo/produced_score", (rdfs___Resource,mo___Score), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Arrangement"


	# Python class properties to wrap the PropertySet objects
	arrangement_of = property(fget=lambda x: x._props["arrangement_of"].get(), fset=lambda x,y : x._props["arrangement_of"].set(y), fdel=None, doc=propDocs["arrangement_of"])
	genre = property(fget=lambda x: x._props["genre"].get(), fset=lambda x,y : x._props["genre"].set(y), fdel=None, doc=propDocs["genre"])
	produced_score = property(fget=lambda x: x._props["produced_score"].get(), fset=lambda x,y : x._props["produced_score"].set(y), fdel=None, doc=propDocs["produced_score"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Composition(event___Event):
	"""
	mo:Composition
	
		A composition event.
		Takes as agent the composer himself.
		It produces a MusicalWork, or a MusicalExpression (when the initial "product" is a score, for example), or both...
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		event___Event.__init__(self)
		self._initialised = False
		self.shortname = "Composition"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["composer"] = PropertySet("composer","http://purl.org/ontology/mo/composer", foaf___Agent, False)
		self._props["genre"] = PropertySet("genre","http://purl.org/ontology/mo/genre", (mo___Genre,rdfs___Resource), False)
		self._props["produced_work"] = PropertySet("produced_work","http://purl.org/ontology/mo/produced_work", (mo___MusicalWork,rdfs___Resource), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Composition"


	# Python class properties to wrap the PropertySet objects
	composer = property(fget=lambda x: x._props["composer"].get(), fset=lambda x,y : x._props["composer"].set(y), fdel=None, doc=propDocs["composer"])
	genre = property(fget=lambda x: x._props["genre"].get(), fset=lambda x,y : x._props["genre"].set(y), fdel=None, doc=propDocs["genre"])
	produced_work = property(fget=lambda x: x._props["produced_work"].get(), fset=lambda x,y : x._props["produced_work"].set(y), fdel=None, doc=propDocs["produced_work"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Festival(event___Event):
	"""
	mo:Festival
	
		A festival - musical/artistic event lasting several days, like Glastonbury, Rock Am Ring...
		We migth decompose this event (which is in fact just a classification of the space/time region related to 
		a particular festival) using hasSubEvent in several performances at different space/time.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		event___Event.__init__(self)
		self._initialised = False
		self.shortname = "Festival"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Festival"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Instrument(rdfs___Resource):
	"""
	mo:Instrument
	
		Any of various devices or contrivances that can be used to produce musical tones or sound.
		
		Any taxonomy can be used to subsume this concept. The default one is one extracted by Ivan Herman
		from the Musicbrainz instrument taxonomy, conforming to SKOS. This concept holds a seeAlso link 
		towards this taxonomy.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Instrument"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["wikipedia"] = PropertySet("wikipedia","http://purl.org/ontology/mo/wikipedia", foaf___Document, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Instrument"


	# Python class properties to wrap the PropertySet objects
	wikipedia = property(fget=lambda x: x._props["wikipedia"].get(), fset=lambda x,y : x._props["wikipedia"].set(y), fdel=None, doc=propDocs["wikipedia"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___MusicalItem(rdfs___Resource):
	"""
	mo:MusicalItem
	A single exemplar of a musical expression.
    
For example, it could be a single exemplar of a CD. This is normally an single object (a CD) possessed by somebody.

From the FRBR final report: The entity defined as item is a concrete entity. It is in many instances a single physical object (e.g., a copy of a one-volume monograph, a single audio cassette, etc.). There are instances, however, where the entity defined as item comprises more than one physical object (e.g., a monograph issued as two separately bound volumes, a recording issued on three separate compact discs, etc.).

In terms of intellectual content and physical form, an item exemplifying a manifestation is normally the same as the manifestation itself. However, variations may occur from one item to another, even when the items exemplify the same manifestation, where those variations are the result of actions external to the intent of the producer of the manifestation (e.g., damage occurring after the item was produced, binding performed by a library, etc.). 
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "MusicalItem"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["encodes"] = PropertySet("encodes","http://purl.org/ontology/mo/encodes", mo___Signal, False)
		self._props["image"] = PropertySet("image","http://purl.org/ontology/mo/image", (foaf___Image,rdfs___Resource), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/MusicalItem"


	# Python class properties to wrap the PropertySet objects
	encodes = property(fget=lambda x: x._props["encodes"].get(), fset=lambda x,y : x._props["encodes"].set(y), fdel=None, doc=propDocs["encodes"])
	image = property(fget=lambda x: x._props["image"].get(), fset=lambda x,y : x._props["image"].set(y), fdel=None, doc=propDocs["image"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Orchestration(mo___Arrangement):
	"""
	mo:Orchestration
	
        	Orchestration includes, in addition to instrumentation, the handling of groups of instruments and their balance and interaction.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Arrangement.__init__(self)
		self._initialised = False
		self.shortname = "Orchestration"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Orchestration"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Recording(event___Event):
	"""
	mo:Recording
	
		A recording event.
		Takes a sound as a factor to produce a signal (analog or digital).
		The location of such events (if any) is the actual location of the corresponding
		microphone or the "recording device".
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		event___Event.__init__(self)
		self._initialised = False
		self.shortname = "Recording"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["engineer"] = PropertySet("engineer","http://purl.org/ontology/mo/engineer", foaf___Agent, False)
		self._props["genre"] = PropertySet("genre","http://purl.org/ontology/mo/genre", (mo___Genre,rdfs___Resource), False)
		self._props["produced_signal"] = PropertySet("produced_signal","http://purl.org/ontology/mo/produced_signal", (mo___Signal,rdfs___Resource), False)
		self._props["recording_of"] = PropertySet("recording_of","http://purl.org/ontology/mo/recording_of", (rdfs___Resource,mo___Sound), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Recording"


	# Python class properties to wrap the PropertySet objects
	engineer = property(fget=lambda x: x._props["engineer"].get(), fset=lambda x,y : x._props["engineer"].set(y), fdel=None, doc=propDocs["engineer"])
	genre = property(fget=lambda x: x._props["genre"].get(), fset=lambda x,y : x._props["genre"].set(y), fdel=None, doc=propDocs["genre"])
	produced_signal = property(fget=lambda x: x._props["produced_signal"].get(), fset=lambda x,y : x._props["produced_signal"].set(y), fdel=None, doc=propDocs["produced_signal"])
	recording_of = property(fget=lambda x: x._props["recording_of"].get(), fset=lambda x,y : x._props["recording_of"].set(y), fdel=None, doc=propDocs["recording_of"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___ReleaseType(rdfs___Resource):
	"""
	mo:ReleaseType
	
		Release type of a particular manifestation, such as "album" or "interview"...
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "ReleaseType"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/ReleaseType"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Show(event___Event):
	"""
	mo:Show
	
		A show - a musical event lasting several days, in a particular venue. Examples can be
		"The Magic Flute" at the Opera Bastille, August 2005, or a musical in the west end...
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		event___Event.__init__(self)
		self._initialised = False
		self.shortname = "Show"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Show"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class frbr___Expression(rdfs___Resource):
	"""
	frbr:Expression
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Expression"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["amazon_asin"] = PropertySet("amazon_asin","http://purl.org/ontology/mo/amazon_asin", foaf___Document, False)
		self._props["licence"] = PropertySet("licence","http://purl.org/ontology/mo/licence", foaf___Document, False)
		self._props["review"] = PropertySet("review","http://purl.org/ontology/mo/review", foaf___Document, False)
		self._props["translation_of"] = PropertySet("translation_of","http://purl.org/ontology/mo/translation_of", frbr___Expression, False)
		self._props["wikipedia"] = PropertySet("wikipedia","http://purl.org/ontology/mo/wikipedia", foaf___Document, False)
		self._initialised = True
	classURI = "http://purl.org/vocab/frbr/core#Expression"


	# Python class properties to wrap the PropertySet objects
	amazon_asin = property(fget=lambda x: x._props["amazon_asin"].get(), fset=lambda x,y : x._props["amazon_asin"].set(y), fdel=None, doc=propDocs["amazon_asin"])
	licence = property(fget=lambda x: x._props["licence"].get(), fset=lambda x,y : x._props["licence"].set(y), fdel=None, doc=propDocs["licence"])
	review = property(fget=lambda x: x._props["review"].get(), fset=lambda x,y : x._props["review"].set(y), fdel=None, doc=propDocs["review"])
	translation_of = property(fget=lambda x: x._props["translation_of"].get(), fset=lambda x,y : x._props["translation_of"].set(y), fdel=None, doc=propDocs["translation_of"])
	wikipedia = property(fget=lambda x: x._props["wikipedia"].get(), fset=lambda x,y : x._props["wikipedia"].set(y), fdel=None, doc=propDocs["wikipedia"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class frbr___Manifestation(rdfs___Resource):
	"""
	frbr:Manifestation
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Manifestation"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["amazon_asin"] = PropertySet("amazon_asin","http://purl.org/ontology/mo/amazon_asin", foaf___Document, False)
		self._props["download"] = PropertySet("download","http://purl.org/ontology/mo/download", foaf___Document, False)
		self._props["free_download"] = PropertySet("free_download","http://purl.org/ontology/mo/free_download", foaf___Document, False)
		self._props["licence"] = PropertySet("licence","http://purl.org/ontology/mo/licence", foaf___Document, False)
		self._props["mailorder"] = PropertySet("mailorder","http://purl.org/ontology/mo/mailorder", foaf___Document, False)
		self._props["paid_download"] = PropertySet("paid_download","http://purl.org/ontology/mo/paid_download", foaf___Document, False)
		self._props["preview_download"] = PropertySet("preview_download","http://purl.org/ontology/mo/preview_download", foaf___Document, False)
		self._props["review"] = PropertySet("review","http://purl.org/ontology/mo/review", foaf___Document, False)
		self._props["wikipedia"] = PropertySet("wikipedia","http://purl.org/ontology/mo/wikipedia", foaf___Document, False)
		self._initialised = True
	classURI = "http://purl.org/vocab/frbr/core#Manifestation"


	# Python class properties to wrap the PropertySet objects
	amazon_asin = property(fget=lambda x: x._props["amazon_asin"].get(), fset=lambda x,y : x._props["amazon_asin"].set(y), fdel=None, doc=propDocs["amazon_asin"])
	download = property(fget=lambda x: x._props["download"].get(), fset=lambda x,y : x._props["download"].set(y), fdel=None, doc=propDocs["download"])
	free_download = property(fget=lambda x: x._props["free_download"].get(), fset=lambda x,y : x._props["free_download"].set(y), fdel=None, doc=propDocs["free_download"])
	licence = property(fget=lambda x: x._props["licence"].get(), fset=lambda x,y : x._props["licence"].set(y), fdel=None, doc=propDocs["licence"])
	mailorder = property(fget=lambda x: x._props["mailorder"].get(), fset=lambda x,y : x._props["mailorder"].set(y), fdel=None, doc=propDocs["mailorder"])
	paid_download = property(fget=lambda x: x._props["paid_download"].get(), fset=lambda x,y : x._props["paid_download"].set(y), fdel=None, doc=propDocs["paid_download"])
	preview_download = property(fget=lambda x: x._props["preview_download"].get(), fset=lambda x,y : x._props["preview_download"].set(y), fdel=None, doc=propDocs["preview_download"])
	review = property(fget=lambda x: x._props["review"].get(), fset=lambda x,y : x._props["review"].set(y), fdel=None, doc=propDocs["review"])
	wikipedia = property(fget=lambda x: x._props["wikipedia"].get(), fset=lambda x,y : x._props["wikipedia"].set(y), fdel=None, doc=propDocs["wikipedia"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class rdfs___Class(rdfs___Resource):
	"""
	rdfs:Class
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Class"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["oneOf"] = PropertySet("oneOf","http://www.w3.org/2002/07/owl#oneOf", rdf___List, False)
		self._initialised = True
	classURI = "http://www.w3.org/2000/01/rdf-schema#Class"


	# Python class properties to wrap the PropertySet objects
	oneOf = property(fget=lambda x: x._props["oneOf"].get(), fset=lambda x,y : x._props["oneOf"].set(y), fdel=None, doc=propDocs["oneOf"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___DateTimeDescription(rdfs___Resource):
	"""
	time:DateTimeDescription
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DateTimeDescription"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["day"] = PropertySet("day","http://www.w3.org/2006/time#day", int, False)
		self._props["dayOfWeek"] = PropertySet("dayOfWeek","http://www.w3.org/2006/time#dayOfWeek", time___DayOfWeek, False)
		self._props["dayOfYear"] = PropertySet("dayOfYear","http://www.w3.org/2006/time#dayOfYear", int, False)
		self._props["hour"] = PropertySet("hour","http://www.w3.org/2006/time#hour", int, False)
		self._props["minute"] = PropertySet("minute","http://www.w3.org/2006/time#minute", int, False)
		self._props["month"] = PropertySet("month","http://www.w3.org/2006/time#month", int, False)
		self._props["second"] = PropertySet("second","http://www.w3.org/2006/time#second", float, False)
		self._props["timeZone"] = PropertySet("timeZone","http://www.w3.org/2006/time#timeZone", tzont___TimeZone, False)
		self._props["unitType"] = PropertySet("unitType","http://www.w3.org/2006/time#unitType", time___TemporalUnit, False)
		self._props["week"] = PropertySet("week","http://www.w3.org/2006/time#week", int, False)
		self._props["year"] = PropertySet("year","http://www.w3.org/2006/time#year", int, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#DateTimeDescription"


	# Python class properties to wrap the PropertySet objects
	day = property(fget=lambda x: x._props["day"].get(), fset=lambda x,y : x._props["day"].set(y), fdel=None, doc=propDocs["day"])
	dayOfWeek = property(fget=lambda x: x._props["dayOfWeek"].get(), fset=lambda x,y : x._props["dayOfWeek"].set(y), fdel=None, doc=propDocs["dayOfWeek"])
	dayOfYear = property(fget=lambda x: x._props["dayOfYear"].get(), fset=lambda x,y : x._props["dayOfYear"].set(y), fdel=None, doc=propDocs["dayOfYear"])
	hour = property(fget=lambda x: x._props["hour"].get(), fset=lambda x,y : x._props["hour"].set(y), fdel=None, doc=propDocs["hour"])
	minute = property(fget=lambda x: x._props["minute"].get(), fset=lambda x,y : x._props["minute"].set(y), fdel=None, doc=propDocs["minute"])
	month = property(fget=lambda x: x._props["month"].get(), fset=lambda x,y : x._props["month"].set(y), fdel=None, doc=propDocs["month"])
	second = property(fget=lambda x: x._props["second"].get(), fset=lambda x,y : x._props["second"].set(y), fdel=None, doc=propDocs["second"])
	timeZone = property(fget=lambda x: x._props["timeZone"].get(), fset=lambda x,y : x._props["timeZone"].set(y), fdel=None, doc=propDocs["timeZone"])
	unitType = property(fget=lambda x: x._props["unitType"].get(), fset=lambda x,y : x._props["unitType"].set(y), fdel=None, doc=propDocs["unitType"])
	week = property(fget=lambda x: x._props["week"].get(), fset=lambda x,y : x._props["week"].set(y), fdel=None, doc=propDocs["week"])
	year = property(fget=lambda x: x._props["year"].get(), fset=lambda x,y : x._props["year"].set(y), fdel=None, doc=propDocs["year"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___DurationDescription(rdfs___Resource):
	"""
	time:DurationDescription
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DurationDescription"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["days"] = PropertySet("days","http://www.w3.org/2006/time#days", float, False)
		self._props["hours"] = PropertySet("hours","http://www.w3.org/2006/time#hours", float, False)
		self._props["minutes"] = PropertySet("minutes","http://www.w3.org/2006/time#minutes", float, False)
		self._props["months"] = PropertySet("months","http://www.w3.org/2006/time#months", float, False)
		self._props["seconds"] = PropertySet("seconds","http://www.w3.org/2006/time#seconds", float, False)
		self._props["weeks"] = PropertySet("weeks","http://www.w3.org/2006/time#weeks", float, False)
		self._props["years"] = PropertySet("years","http://www.w3.org/2006/time#years", float, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#DurationDescription"


	# Python class properties to wrap the PropertySet objects
	days = property(fget=lambda x: x._props["days"].get(), fset=lambda x,y : x._props["days"].set(y), fdel=None, doc=propDocs["days"])
	hours = property(fget=lambda x: x._props["hours"].get(), fset=lambda x,y : x._props["hours"].set(y), fdel=None, doc=propDocs["hours"])
	minutes = property(fget=lambda x: x._props["minutes"].get(), fset=lambda x,y : x._props["minutes"].set(y), fdel=None, doc=propDocs["minutes"])
	months = property(fget=lambda x: x._props["months"].get(), fset=lambda x,y : x._props["months"].set(y), fdel=None, doc=propDocs["months"])
	seconds = property(fget=lambda x: x._props["seconds"].get(), fset=lambda x,y : x._props["seconds"].set(y), fdel=None, doc=propDocs["seconds"])
	weeks = property(fget=lambda x: x._props["weeks"].get(), fset=lambda x,y : x._props["weeks"].set(y), fdel=None, doc=propDocs["weeks"])
	years = property(fget=lambda x: x._props["years"].get(), fset=lambda x,y : x._props["years"].set(y), fdel=None, doc=propDocs["years"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___Interval(time___TemporalEntity):
	"""
	time:Interval
	 A time interval (eg. "the year 1994")
	"""
	def __init__(self,URI=None):
		# Initialise parents
		time___TemporalEntity.__init__(self)
		self._initialised = False
		self.shortname = "Interval"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["beginsAtDateTime"] = PropertySet("beginsAtDateTime","http://purl.org/NET/c4dm/timeline.owl#beginsAtDateTime", str, True)
		self._props["beginsAtDuration"] = PropertySet("beginsAtDuration","http://purl.org/NET/c4dm/timeline.owl#beginsAtDuration", str, True)
		self._props["durationXSD"] = PropertySet("durationXSD","http://purl.org/NET/c4dm/timeline.owl#durationXSD", str, True)
		self._props["onTimeLine"] = PropertySet("onTimeLine","http://purl.org/NET/c4dm/timeline.owl#onTimeLine", timeline___TimeLine, False)
		self._props["inside"] = PropertySet("inside","http://www.w3.org/2006/time#inside", time___Instant, False)
		self._props["intervalAfter"] = PropertySet("intervalAfter","http://www.w3.org/2006/time#intervalAfter", None, False)
		self._props["intervalBefore"] = PropertySet("intervalBefore","http://www.w3.org/2006/time#intervalBefore", (time___ProperInterval,time___TemporalEntity,time___Interval), False)
		self._props["intervalContains"] = PropertySet("intervalContains","http://www.w3.org/2006/time#intervalContains", None, False)
		self._props["intervalDuring"] = PropertySet("intervalDuring","http://www.w3.org/2006/time#intervalDuring", (time___ProperInterval,time___Interval), False)
		self._props["intervalMeets"] = PropertySet("intervalMeets","http://www.w3.org/2006/time#intervalMeets", (time___ProperInterval,time___Interval), False)
		self._props["intervalMetBy"] = PropertySet("intervalMetBy","http://www.w3.org/2006/time#intervalMetBy", None, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#Interval"


	# Python class properties to wrap the PropertySet objects
	beginsAtDateTime = property(fget=lambda x: x._props["beginsAtDateTime"].get(), fset=lambda x,y : x._props["beginsAtDateTime"].set(y), fdel=None, doc=propDocs["beginsAtDateTime"])
	beginsAtDuration = property(fget=lambda x: x._props["beginsAtDuration"].get(), fset=lambda x,y : x._props["beginsAtDuration"].set(y), fdel=None, doc=propDocs["beginsAtDuration"])
	durationXSD = property(fget=lambda x: x._props["durationXSD"].get(), fset=lambda x,y : x._props["durationXSD"].set(y), fdel=None, doc=propDocs["durationXSD"])
	onTimeLine = property(fget=lambda x: x._props["onTimeLine"].get(), fset=lambda x,y : x._props["onTimeLine"].set(y), fdel=None, doc=propDocs["onTimeLine"])
	inside = property(fget=lambda x: x._props["inside"].get(), fset=lambda x,y : x._props["inside"].set(y), fdel=None, doc=propDocs["inside"])
	intervalAfter = property(fget=lambda x: x._props["intervalAfter"].get(), fset=lambda x,y : x._props["intervalAfter"].set(y), fdel=None, doc=propDocs["intervalAfter"])
	intervalBefore = property(fget=lambda x: x._props["intervalBefore"].get(), fset=lambda x,y : x._props["intervalBefore"].set(y), fdel=None, doc=propDocs["intervalBefore"])
	intervalContains = property(fget=lambda x: x._props["intervalContains"].get(), fset=lambda x,y : x._props["intervalContains"].set(y), fdel=None, doc=propDocs["intervalContains"])
	intervalDuring = property(fget=lambda x: x._props["intervalDuring"].get(), fset=lambda x,y : x._props["intervalDuring"].set(y), fdel=None, doc=propDocs["intervalDuring"])
	intervalMeets = property(fget=lambda x: x._props["intervalMeets"].get(), fset=lambda x,y : x._props["intervalMeets"].set(y), fdel=None, doc=propDocs["intervalMeets"])
	intervalMetBy = property(fget=lambda x: x._props["intervalMetBy"].get(), fset=lambda x,y : x._props["intervalMetBy"].set(y), fdel=None, doc=propDocs["intervalMetBy"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___ProperInterval(time___Interval):
	"""
	time:ProperInterval
	"""
	def __init__(self,URI=None):
		# Initialise parents
		time___Interval.__init__(self)
		self._initialised = False
		self.shortname = "ProperInterval"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["at"] = PropertySet("at","http://purl.org/NET/c4dm/timeline.owl#at", None, False)
		self._props["atDate"] = PropertySet("atDate","http://purl.org/NET/c4dm/timeline.owl#atDate", str, False)
		self._props["atDateTime"] = PropertySet("atDateTime","http://purl.org/NET/c4dm/timeline.owl#atDateTime", str, True)
		self._props["atDuration"] = PropertySet("atDuration","http://purl.org/NET/c4dm/timeline.owl#atDuration", str, True)
		self._props["atInt"] = PropertySet("atInt","http://purl.org/NET/c4dm/timeline.owl#atInt", int, False)
		self._props["atReal"] = PropertySet("atReal","http://purl.org/NET/c4dm/timeline.owl#atReal", float, False)
		self._props["atYear"] = PropertySet("atYear","http://purl.org/NET/c4dm/timeline.owl#atYear", int, False)
		self._props["atYearMonth"] = PropertySet("atYearMonth","http://purl.org/NET/c4dm/timeline.owl#atYearMonth", str, False)
		self._props["beginsAt"] = PropertySet("beginsAt","http://purl.org/NET/c4dm/timeline.owl#beginsAt", None, False)
		self._props["beginsAtDateTime"] = PropertySet("beginsAtDateTime","http://purl.org/NET/c4dm/timeline.owl#beginsAtDateTime", str, True)
		self._props["beginsAtDuration"] = PropertySet("beginsAtDuration","http://purl.org/NET/c4dm/timeline.owl#beginsAtDuration", str, True)
		self._props["beginsAtInt"] = PropertySet("beginsAtInt","http://purl.org/NET/c4dm/timeline.owl#beginsAtInt", int, False)
		self._props["duration"] = PropertySet("duration","http://purl.org/NET/c4dm/timeline.owl#duration", None, False)
		self._props["durationInt"] = PropertySet("durationInt","http://purl.org/NET/c4dm/timeline.owl#durationInt", int, False)
		self._props["durationXSD"] = PropertySet("durationXSD","http://purl.org/NET/c4dm/timeline.owl#durationXSD", str, True)
		self._props["endsAt"] = PropertySet("endsAt","http://purl.org/NET/c4dm/timeline.owl#endsAt", None, False)
		self._props["endsAtDateTime"] = PropertySet("endsAtDateTime","http://purl.org/NET/c4dm/timeline.owl#endsAtDateTime", str, False)
		self._props["endsAtDuration"] = PropertySet("endsAtDuration","http://purl.org/NET/c4dm/timeline.owl#endsAtDuration", str, False)
		self._props["endsAtInt"] = PropertySet("endsAtInt","http://purl.org/NET/c4dm/timeline.owl#endsAtInt", int, False)
		self._props["onTimeLine"] = PropertySet("onTimeLine","http://purl.org/NET/c4dm/timeline.owl#onTimeLine", timeline___TimeLine, False)
		self._props["intervalAfter"] = PropertySet("intervalAfter","http://www.w3.org/2006/time#intervalAfter", None, False)
		self._props["intervalBefore"] = PropertySet("intervalBefore","http://www.w3.org/2006/time#intervalBefore", (time___ProperInterval,time___TemporalEntity,time___Interval), False)
		self._props["intervalContains"] = PropertySet("intervalContains","http://www.w3.org/2006/time#intervalContains", None, False)
		self._props["intervalDuring"] = PropertySet("intervalDuring","http://www.w3.org/2006/time#intervalDuring", (time___ProperInterval,time___Interval), False)
		self._props["intervalEquals"] = PropertySet("intervalEquals","http://www.w3.org/2006/time#intervalEquals", time___ProperInterval, False)
		self._props["intervalFinishedBy"] = PropertySet("intervalFinishedBy","http://www.w3.org/2006/time#intervalFinishedBy", None, False)
		self._props["intervalFinishes"] = PropertySet("intervalFinishes","http://www.w3.org/2006/time#intervalFinishes", time___ProperInterval, False)
		self._props["intervalMeets"] = PropertySet("intervalMeets","http://www.w3.org/2006/time#intervalMeets", (time___ProperInterval,time___Interval), False)
		self._props["intervalMetBy"] = PropertySet("intervalMetBy","http://www.w3.org/2006/time#intervalMetBy", None, False)
		self._props["intervalOverlappedBy"] = PropertySet("intervalOverlappedBy","http://www.w3.org/2006/time#intervalOverlappedBy", None, False)
		self._props["intervalOverlaps"] = PropertySet("intervalOverlaps","http://www.w3.org/2006/time#intervalOverlaps", time___ProperInterval, False)
		self._props["intervalStartedBy"] = PropertySet("intervalStartedBy","http://www.w3.org/2006/time#intervalStartedBy", None, False)
		self._props["intervalStarts"] = PropertySet("intervalStarts","http://www.w3.org/2006/time#intervalStarts", time___ProperInterval, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#ProperInterval"


	# Python class properties to wrap the PropertySet objects
	at = property(fget=lambda x: x._props["at"].get(), fset=lambda x,y : x._props["at"].set(y), fdel=None, doc=propDocs["at"])
	atDate = property(fget=lambda x: x._props["atDate"].get(), fset=lambda x,y : x._props["atDate"].set(y), fdel=None, doc=propDocs["atDate"])
	atDateTime = property(fget=lambda x: x._props["atDateTime"].get(), fset=lambda x,y : x._props["atDateTime"].set(y), fdel=None, doc=propDocs["atDateTime"])
	atDuration = property(fget=lambda x: x._props["atDuration"].get(), fset=lambda x,y : x._props["atDuration"].set(y), fdel=None, doc=propDocs["atDuration"])
	atInt = property(fget=lambda x: x._props["atInt"].get(), fset=lambda x,y : x._props["atInt"].set(y), fdel=None, doc=propDocs["atInt"])
	atReal = property(fget=lambda x: x._props["atReal"].get(), fset=lambda x,y : x._props["atReal"].set(y), fdel=None, doc=propDocs["atReal"])
	atYear = property(fget=lambda x: x._props["atYear"].get(), fset=lambda x,y : x._props["atYear"].set(y), fdel=None, doc=propDocs["atYear"])
	atYearMonth = property(fget=lambda x: x._props["atYearMonth"].get(), fset=lambda x,y : x._props["atYearMonth"].set(y), fdel=None, doc=propDocs["atYearMonth"])
	beginsAt = property(fget=lambda x: x._props["beginsAt"].get(), fset=lambda x,y : x._props["beginsAt"].set(y), fdel=None, doc=propDocs["beginsAt"])
	beginsAtDateTime = property(fget=lambda x: x._props["beginsAtDateTime"].get(), fset=lambda x,y : x._props["beginsAtDateTime"].set(y), fdel=None, doc=propDocs["beginsAtDateTime"])
	beginsAtDuration = property(fget=lambda x: x._props["beginsAtDuration"].get(), fset=lambda x,y : x._props["beginsAtDuration"].set(y), fdel=None, doc=propDocs["beginsAtDuration"])
	beginsAtInt = property(fget=lambda x: x._props["beginsAtInt"].get(), fset=lambda x,y : x._props["beginsAtInt"].set(y), fdel=None, doc=propDocs["beginsAtInt"])
	duration = property(fget=lambda x: x._props["duration"].get(), fset=lambda x,y : x._props["duration"].set(y), fdel=None, doc=propDocs["duration"])
	durationInt = property(fget=lambda x: x._props["durationInt"].get(), fset=lambda x,y : x._props["durationInt"].set(y), fdel=None, doc=propDocs["durationInt"])
	durationXSD = property(fget=lambda x: x._props["durationXSD"].get(), fset=lambda x,y : x._props["durationXSD"].set(y), fdel=None, doc=propDocs["durationXSD"])
	endsAt = property(fget=lambda x: x._props["endsAt"].get(), fset=lambda x,y : x._props["endsAt"].set(y), fdel=None, doc=propDocs["endsAt"])
	endsAtDateTime = property(fget=lambda x: x._props["endsAtDateTime"].get(), fset=lambda x,y : x._props["endsAtDateTime"].set(y), fdel=None, doc=propDocs["endsAtDateTime"])
	endsAtDuration = property(fget=lambda x: x._props["endsAtDuration"].get(), fset=lambda x,y : x._props["endsAtDuration"].set(y), fdel=None, doc=propDocs["endsAtDuration"])
	endsAtInt = property(fget=lambda x: x._props["endsAtInt"].get(), fset=lambda x,y : x._props["endsAtInt"].set(y), fdel=None, doc=propDocs["endsAtInt"])
	onTimeLine = property(fget=lambda x: x._props["onTimeLine"].get(), fset=lambda x,y : x._props["onTimeLine"].set(y), fdel=None, doc=propDocs["onTimeLine"])
	intervalAfter = property(fget=lambda x: x._props["intervalAfter"].get(), fset=lambda x,y : x._props["intervalAfter"].set(y), fdel=None, doc=propDocs["intervalAfter"])
	intervalBefore = property(fget=lambda x: x._props["intervalBefore"].get(), fset=lambda x,y : x._props["intervalBefore"].set(y), fdel=None, doc=propDocs["intervalBefore"])
	intervalContains = property(fget=lambda x: x._props["intervalContains"].get(), fset=lambda x,y : x._props["intervalContains"].set(y), fdel=None, doc=propDocs["intervalContains"])
	intervalDuring = property(fget=lambda x: x._props["intervalDuring"].get(), fset=lambda x,y : x._props["intervalDuring"].set(y), fdel=None, doc=propDocs["intervalDuring"])
	intervalEquals = property(fget=lambda x: x._props["intervalEquals"].get(), fset=lambda x,y : x._props["intervalEquals"].set(y), fdel=None, doc=propDocs["intervalEquals"])
	intervalFinishedBy = property(fget=lambda x: x._props["intervalFinishedBy"].get(), fset=lambda x,y : x._props["intervalFinishedBy"].set(y), fdel=None, doc=propDocs["intervalFinishedBy"])
	intervalFinishes = property(fget=lambda x: x._props["intervalFinishes"].get(), fset=lambda x,y : x._props["intervalFinishes"].set(y), fdel=None, doc=propDocs["intervalFinishes"])
	intervalMeets = property(fget=lambda x: x._props["intervalMeets"].get(), fset=lambda x,y : x._props["intervalMeets"].set(y), fdel=None, doc=propDocs["intervalMeets"])
	intervalMetBy = property(fget=lambda x: x._props["intervalMetBy"].get(), fset=lambda x,y : x._props["intervalMetBy"].set(y), fdel=None, doc=propDocs["intervalMetBy"])
	intervalOverlappedBy = property(fget=lambda x: x._props["intervalOverlappedBy"].get(), fset=lambda x,y : x._props["intervalOverlappedBy"].set(y), fdel=None, doc=propDocs["intervalOverlappedBy"])
	intervalOverlaps = property(fget=lambda x: x._props["intervalOverlaps"].get(), fset=lambda x,y : x._props["intervalOverlaps"].set(y), fdel=None, doc=propDocs["intervalOverlaps"])
	intervalStartedBy = property(fget=lambda x: x._props["intervalStartedBy"].get(), fset=lambda x,y : x._props["intervalStartedBy"].set(y), fdel=None, doc=propDocs["intervalStartedBy"])
	intervalStarts = property(fget=lambda x: x._props["intervalStarts"].get(), fset=lambda x,y : x._props["intervalStarts"].set(y), fdel=None, doc=propDocs["intervalStarts"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___Year(time___DurationDescription):
	"""
	time:Year
	"""
	def __init__(self,URI=None):
		# Initialise parents
		time___DurationDescription.__init__(self)
		self._initialised = False
		self.shortname = "Year"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#Year"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___OnlineChatAccount(foaf___OnlineAccount):
	"""
	foaf:OnlineChatAccount
	An online chat account.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___OnlineAccount.__init__(self)
		self._initialised = False
		self.shortname = "OnlineChatAccount"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/OnlineChatAccount"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Project(rdfs___Resource):
	"""
	foaf:Project
	A project (a collective endeavour of some kind).
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Project"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Project"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class event___Factor(rdfs___Resource):
	"""
	event:Factor
	
		Everything used as a factor in an event
		
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Factor"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/event.owl#Factor"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___AbstractInstant(timeline___Instant):
	"""
	timeline:AbstractInstant
	An instant defined on an abstract timeline
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___Instant.__init__(self)
		self._initialised = False
		self.shortname = "AbstractInstant"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#AbstractInstant"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___AbstractTimeLine(timeline___TimeLine):
	"""
	timeline:AbstractTimeLine
	
    	Abstract time lines may be used as a backbone for Score, Works, ... 
	This allows for TimeLine maps to relate works to a given 
	performance (this part was played at this time).
	
		Abstract time lines may be used as a backbone for Score, Works, ... 
		This allows for TimeLine maps to relate works to a given performance (this note was played at this time).
		No coordinate systems are defined for these timelines. Their structure is implicitly defined
		by the relations between time objects defined on them (eg. this note is before this note, which is
		before this silent, which is at the same time as this note).
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___TimeLine.__init__(self)
		self._initialised = False
		self.shortname = "AbstractTimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#AbstractTimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___DiscreteInterval(rdfs___Resource):
	"""
	timeline:DiscreteInterval
	An interval defined on a discrete timeline, like the one backing a digital signal
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "DiscreteInterval"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#DiscreteInterval"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___Interval(time___Interval):
	"""
	timeline:Interval
	An interval (same as in OWL-Time). Allen's relationships are defined in OWL-Time.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		time___Interval.__init__(self)
		self._initialised = False
		self.shortname = "Interval"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["at"] = PropertySet("at","http://purl.org/NET/c4dm/timeline.owl#at", None, False)
		self._props["atDate"] = PropertySet("atDate","http://purl.org/NET/c4dm/timeline.owl#atDate", str, False)
		self._props["atDateTime"] = PropertySet("atDateTime","http://purl.org/NET/c4dm/timeline.owl#atDateTime", str, True)
		self._props["atDuration"] = PropertySet("atDuration","http://purl.org/NET/c4dm/timeline.owl#atDuration", str, True)
		self._props["atInt"] = PropertySet("atInt","http://purl.org/NET/c4dm/timeline.owl#atInt", int, False)
		self._props["atReal"] = PropertySet("atReal","http://purl.org/NET/c4dm/timeline.owl#atReal", float, False)
		self._props["atYear"] = PropertySet("atYear","http://purl.org/NET/c4dm/timeline.owl#atYear", int, False)
		self._props["atYearMonth"] = PropertySet("atYearMonth","http://purl.org/NET/c4dm/timeline.owl#atYearMonth", str, False)
		self._props["beginsAt"] = PropertySet("beginsAt","http://purl.org/NET/c4dm/timeline.owl#beginsAt", None, False)
		self._props["beginsAtDateTime"] = PropertySet("beginsAtDateTime","http://purl.org/NET/c4dm/timeline.owl#beginsAtDateTime", str, True)
		self._props["beginsAtDuration"] = PropertySet("beginsAtDuration","http://purl.org/NET/c4dm/timeline.owl#beginsAtDuration", str, True)
		self._props["beginsAtInt"] = PropertySet("beginsAtInt","http://purl.org/NET/c4dm/timeline.owl#beginsAtInt", int, False)
		self._props["duration"] = PropertySet("duration","http://purl.org/NET/c4dm/timeline.owl#duration", None, False)
		self._props["durationInt"] = PropertySet("durationInt","http://purl.org/NET/c4dm/timeline.owl#durationInt", int, False)
		self._props["durationXSD"] = PropertySet("durationXSD","http://purl.org/NET/c4dm/timeline.owl#durationXSD", str, True)
		self._props["endsAt"] = PropertySet("endsAt","http://purl.org/NET/c4dm/timeline.owl#endsAt", None, False)
		self._props["endsAtDateTime"] = PropertySet("endsAtDateTime","http://purl.org/NET/c4dm/timeline.owl#endsAtDateTime", str, False)
		self._props["endsAtDuration"] = PropertySet("endsAtDuration","http://purl.org/NET/c4dm/timeline.owl#endsAtDuration", str, False)
		self._props["endsAtInt"] = PropertySet("endsAtInt","http://purl.org/NET/c4dm/timeline.owl#endsAtInt", int, False)
		self._props["onTimeLine"] = PropertySet("onTimeLine","http://purl.org/NET/c4dm/timeline.owl#onTimeLine", timeline___TimeLine, False)
		self._props["intervalAfter"] = PropertySet("intervalAfter","http://www.w3.org/2006/time#intervalAfter", None, False)
		self._props["intervalBefore"] = PropertySet("intervalBefore","http://www.w3.org/2006/time#intervalBefore", (time___ProperInterval,time___TemporalEntity,time___Interval), False)
		self._props["intervalContains"] = PropertySet("intervalContains","http://www.w3.org/2006/time#intervalContains", None, False)
		self._props["intervalDuring"] = PropertySet("intervalDuring","http://www.w3.org/2006/time#intervalDuring", (time___ProperInterval,time___Interval), False)
		self._props["intervalEquals"] = PropertySet("intervalEquals","http://www.w3.org/2006/time#intervalEquals", time___ProperInterval, False)
		self._props["intervalFinishedBy"] = PropertySet("intervalFinishedBy","http://www.w3.org/2006/time#intervalFinishedBy", None, False)
		self._props["intervalFinishes"] = PropertySet("intervalFinishes","http://www.w3.org/2006/time#intervalFinishes", time___ProperInterval, False)
		self._props["intervalMeets"] = PropertySet("intervalMeets","http://www.w3.org/2006/time#intervalMeets", (time___ProperInterval,time___Interval), False)
		self._props["intervalMetBy"] = PropertySet("intervalMetBy","http://www.w3.org/2006/time#intervalMetBy", None, False)
		self._props["intervalOverlappedBy"] = PropertySet("intervalOverlappedBy","http://www.w3.org/2006/time#intervalOverlappedBy", None, False)
		self._props["intervalOverlaps"] = PropertySet("intervalOverlaps","http://www.w3.org/2006/time#intervalOverlaps", time___ProperInterval, False)
		self._props["intervalStartedBy"] = PropertySet("intervalStartedBy","http://www.w3.org/2006/time#intervalStartedBy", None, False)
		self._props["intervalStarts"] = PropertySet("intervalStarts","http://www.w3.org/2006/time#intervalStarts", time___ProperInterval, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#Interval"


	# Python class properties to wrap the PropertySet objects
	at = property(fget=lambda x: x._props["at"].get(), fset=lambda x,y : x._props["at"].set(y), fdel=None, doc=propDocs["at"])
	atDate = property(fget=lambda x: x._props["atDate"].get(), fset=lambda x,y : x._props["atDate"].set(y), fdel=None, doc=propDocs["atDate"])
	atDateTime = property(fget=lambda x: x._props["atDateTime"].get(), fset=lambda x,y : x._props["atDateTime"].set(y), fdel=None, doc=propDocs["atDateTime"])
	atDuration = property(fget=lambda x: x._props["atDuration"].get(), fset=lambda x,y : x._props["atDuration"].set(y), fdel=None, doc=propDocs["atDuration"])
	atInt = property(fget=lambda x: x._props["atInt"].get(), fset=lambda x,y : x._props["atInt"].set(y), fdel=None, doc=propDocs["atInt"])
	atReal = property(fget=lambda x: x._props["atReal"].get(), fset=lambda x,y : x._props["atReal"].set(y), fdel=None, doc=propDocs["atReal"])
	atYear = property(fget=lambda x: x._props["atYear"].get(), fset=lambda x,y : x._props["atYear"].set(y), fdel=None, doc=propDocs["atYear"])
	atYearMonth = property(fget=lambda x: x._props["atYearMonth"].get(), fset=lambda x,y : x._props["atYearMonth"].set(y), fdel=None, doc=propDocs["atYearMonth"])
	beginsAt = property(fget=lambda x: x._props["beginsAt"].get(), fset=lambda x,y : x._props["beginsAt"].set(y), fdel=None, doc=propDocs["beginsAt"])
	beginsAtDateTime = property(fget=lambda x: x._props["beginsAtDateTime"].get(), fset=lambda x,y : x._props["beginsAtDateTime"].set(y), fdel=None, doc=propDocs["beginsAtDateTime"])
	beginsAtDuration = property(fget=lambda x: x._props["beginsAtDuration"].get(), fset=lambda x,y : x._props["beginsAtDuration"].set(y), fdel=None, doc=propDocs["beginsAtDuration"])
	beginsAtInt = property(fget=lambda x: x._props["beginsAtInt"].get(), fset=lambda x,y : x._props["beginsAtInt"].set(y), fdel=None, doc=propDocs["beginsAtInt"])
	duration = property(fget=lambda x: x._props["duration"].get(), fset=lambda x,y : x._props["duration"].set(y), fdel=None, doc=propDocs["duration"])
	durationInt = property(fget=lambda x: x._props["durationInt"].get(), fset=lambda x,y : x._props["durationInt"].set(y), fdel=None, doc=propDocs["durationInt"])
	durationXSD = property(fget=lambda x: x._props["durationXSD"].get(), fset=lambda x,y : x._props["durationXSD"].set(y), fdel=None, doc=propDocs["durationXSD"])
	endsAt = property(fget=lambda x: x._props["endsAt"].get(), fset=lambda x,y : x._props["endsAt"].set(y), fdel=None, doc=propDocs["endsAt"])
	endsAtDateTime = property(fget=lambda x: x._props["endsAtDateTime"].get(), fset=lambda x,y : x._props["endsAtDateTime"].set(y), fdel=None, doc=propDocs["endsAtDateTime"])
	endsAtDuration = property(fget=lambda x: x._props["endsAtDuration"].get(), fset=lambda x,y : x._props["endsAtDuration"].set(y), fdel=None, doc=propDocs["endsAtDuration"])
	endsAtInt = property(fget=lambda x: x._props["endsAtInt"].get(), fset=lambda x,y : x._props["endsAtInt"].set(y), fdel=None, doc=propDocs["endsAtInt"])
	onTimeLine = property(fget=lambda x: x._props["onTimeLine"].get(), fset=lambda x,y : x._props["onTimeLine"].set(y), fdel=None, doc=propDocs["onTimeLine"])
	intervalAfter = property(fget=lambda x: x._props["intervalAfter"].get(), fset=lambda x,y : x._props["intervalAfter"].set(y), fdel=None, doc=propDocs["intervalAfter"])
	intervalBefore = property(fget=lambda x: x._props["intervalBefore"].get(), fset=lambda x,y : x._props["intervalBefore"].set(y), fdel=None, doc=propDocs["intervalBefore"])
	intervalContains = property(fget=lambda x: x._props["intervalContains"].get(), fset=lambda x,y : x._props["intervalContains"].set(y), fdel=None, doc=propDocs["intervalContains"])
	intervalDuring = property(fget=lambda x: x._props["intervalDuring"].get(), fset=lambda x,y : x._props["intervalDuring"].set(y), fdel=None, doc=propDocs["intervalDuring"])
	intervalEquals = property(fget=lambda x: x._props["intervalEquals"].get(), fset=lambda x,y : x._props["intervalEquals"].set(y), fdel=None, doc=propDocs["intervalEquals"])
	intervalFinishedBy = property(fget=lambda x: x._props["intervalFinishedBy"].get(), fset=lambda x,y : x._props["intervalFinishedBy"].set(y), fdel=None, doc=propDocs["intervalFinishedBy"])
	intervalFinishes = property(fget=lambda x: x._props["intervalFinishes"].get(), fset=lambda x,y : x._props["intervalFinishes"].set(y), fdel=None, doc=propDocs["intervalFinishes"])
	intervalMeets = property(fget=lambda x: x._props["intervalMeets"].get(), fset=lambda x,y : x._props["intervalMeets"].set(y), fdel=None, doc=propDocs["intervalMeets"])
	intervalMetBy = property(fget=lambda x: x._props["intervalMetBy"].get(), fset=lambda x,y : x._props["intervalMetBy"].set(y), fdel=None, doc=propDocs["intervalMetBy"])
	intervalOverlappedBy = property(fget=lambda x: x._props["intervalOverlappedBy"].get(), fset=lambda x,y : x._props["intervalOverlappedBy"].set(y), fdel=None, doc=propDocs["intervalOverlappedBy"])
	intervalOverlaps = property(fget=lambda x: x._props["intervalOverlaps"].get(), fset=lambda x,y : x._props["intervalOverlaps"].set(y), fdel=None, doc=propDocs["intervalOverlaps"])
	intervalStartedBy = property(fget=lambda x: x._props["intervalStartedBy"].get(), fset=lambda x,y : x._props["intervalStartedBy"].set(y), fdel=None, doc=propDocs["intervalStartedBy"])
	intervalStarts = property(fget=lambda x: x._props["intervalStarts"].get(), fset=lambda x,y : x._props["intervalStarts"].set(y), fdel=None, doc=propDocs["intervalStarts"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___RelativeInterval(rdfs___Resource):
	"""
	timeline:RelativeInterval
	an interval defined on a relative timeline
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "RelativeInterval"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#RelativeInterval"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___TimeLineMap(rdfs___Resource):
	"""
	timeline:TimeLineMap
	Allows to map two time lines together
	
		Two time lines can be related, such as the one backing a continuous signal and
		the one backing the digitized signal. This sort of relation is expressed through an instance
		of a TimeLine map (eg. "the timeline backing this signal corresponds
		to the physical timeline: point 0 on this timeline corresponds to the
		20th of december at 5pm").
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TimeLineMap"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["domainTimeLine"] = PropertySet("domainTimeLine","http://purl.org/NET/c4dm/timeline.owl#domainTimeLine", timeline___TimeLine, False)
		self._props["rangeTimeLine"] = PropertySet("rangeTimeLine","http://purl.org/NET/c4dm/timeline.owl#rangeTimeLine", timeline___TimeLine, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#TimeLineMap"


	# Python class properties to wrap the PropertySet objects
	domainTimeLine = property(fget=lambda x: x._props["domainTimeLine"].get(), fset=lambda x,y : x._props["domainTimeLine"].set(y), fdel=None, doc=propDocs["domainTimeLine"])
	rangeTimeLine = property(fget=lambda x: x._props["rangeTimeLine"].get(), fset=lambda x,y : x._props["rangeTimeLine"].set(y), fdel=None, doc=propDocs["rangeTimeLine"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___UniformSamplingMap(timeline___TimeLineMap):
	"""
	timeline:UniformSamplingMap
	Describe the relation between a continuous time-line and its sampled equivalent
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___TimeLineMap.__init__(self)
		self._initialised = False
		self.shortname = "UniformSamplingMap"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["sampleRate"] = PropertySet("sampleRate","http://purl.org/NET/c4dm/timeline.owl#sampleRate", int, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#UniformSamplingMap"


	# Python class properties to wrap the PropertySet objects
	sampleRate = property(fget=lambda x: x._props["sampleRate"].get(), fset=lambda x,y : x._props["sampleRate"].set(y), fdel=None, doc=propDocs["sampleRate"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class chord___ChordEvent(event___Event):
	"""
	chord:ChordEvent
	A chord being played.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		event___Event.__init__(self)
		self._initialised = False
		self.shortname = "ChordEvent"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["chord"] = PropertySet("chord","http://purl.org/ontology/chord/chord", chord___Chord, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/chord/ChordEvent"


	# Python class properties to wrap the PropertySet objects
	chord = property(fget=lambda x: x._props["chord"].get(), fset=lambda x,y : x._props["chord"].set(y), fdel=None, doc=propDocs["chord"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class chord___Natural(chord___Note):
	"""
	chord:Natural
	One of the seven natural notes of the Western music system.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		chord___Note.__init__(self)
		self._initialised = False
		self.shortname = "Natural"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/chord/Natural"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Genre(rdfs___Resource):
	"""
	mo:Genre
	
		An expressive style of music.
		
		Any taxonomy can be plug-in here. You can either define a genre by yourself, like this:

		:mygenre a mo:Genre; dc:title "electro rock".

		Or you can refer to a DBPedia genre (such as http://dbpedia.org/resource/Baroque_music), allowing semantic web
		clients to access easily really detailed structured information about the genre you are refering to.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Genre"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["similar_to"] = PropertySet("similar_to","http://purl.org/ontology/mo/similar_to", (foaf___Agent,mo___Genre,mo___Signal), False)
		self._props["wikipedia"] = PropertySet("wikipedia","http://purl.org/ontology/mo/wikipedia", foaf___Document, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Genre"


	# Python class properties to wrap the PropertySet objects
	similar_to = property(fget=lambda x: x._props["similar_to"].get(), fset=lambda x,y : x._props["similar_to"].set(y), fdel=None, doc=propDocs["similar_to"])
	wikipedia = property(fget=lambda x: x._props["wikipedia"].get(), fset=lambda x,y : x._props["wikipedia"].set(y), fdel=None, doc=propDocs["wikipedia"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Medium(mo___MusicalItem):
	"""
	mo:Medium
	A means or instrumentality for storing or communicating musical manifestation.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicalItem.__init__(self)
		self._initialised = False
		self.shortname = "Medium"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Medium"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___MusicalExpression(frbr___Expression):
	"""
	mo:MusicalExpression
	
The intellectual or artistic realization of a work in the form of alpha-numeric, musical, or choreographic notation, sound, etc., or any combination of such forms.    


For example:

Work #1 Franz Schubert's Trout quintet

    * Expression #1 the composer's score
    * Expression #2 sound issued from the performance by the Amadeus Quartet and Hephzibah Menuhin on piano
    * Expression #3 sound issued from the performance by the Cleveland Quartet and Yo-Yo Ma on the cello
    * . . . . 

The Music Ontology defines the following sub-concepts of a MusicalExpression, which should be used instead of MusicalExpression itself: Score (the
result of an arrangement), Sound (produced during a performance), Signal. However, it is possible to stick to FRBR and bypass the worflow
mechanism this ontology defines by using the core FRBR properties on such objects. But it is often better to use events to interconnect such 
expressions (allowing to go deeply into the production process - `this performer was playing this particular instrument at that
particular time').
	
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		frbr___Expression.__init__(self)
		self._initialised = False
		self.shortname = "MusicalExpression"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["discogs"] = PropertySet("discogs","http://purl.org/ontology/mo/discogs", foaf___Document, False)
		self._props["image"] = PropertySet("image","http://purl.org/ontology/mo/image", (foaf___Image,rdfs___Resource), False)
		self._props["imdb"] = PropertySet("imdb","http://purl.org/ontology/mo/imdb", foaf___Document, False)
		self._props["manifestation"] = PropertySet("manifestation","http://purl.org/ontology/mo/manifestation", mo___MusicalManifestation, False)
		self._props["musicmoz"] = PropertySet("musicmoz","http://purl.org/ontology/mo/musicmoz", foaf___Document, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/MusicalExpression"


	# Python class properties to wrap the PropertySet objects
	discogs = property(fget=lambda x: x._props["discogs"].get(), fset=lambda x,y : x._props["discogs"].set(y), fdel=None, doc=propDocs["discogs"])
	image = property(fget=lambda x: x._props["image"].get(), fset=lambda x,y : x._props["image"].set(y), fdel=None, doc=propDocs["image"])
	imdb = property(fget=lambda x: x._props["imdb"].get(), fset=lambda x,y : x._props["imdb"].set(y), fdel=None, doc=propDocs["imdb"])
	manifestation = property(fget=lambda x: x._props["manifestation"].get(), fset=lambda x,y : x._props["manifestation"].set(y), fdel=None, doc=propDocs["manifestation"])
	musicmoz = property(fget=lambda x: x._props["musicmoz"].get(), fset=lambda x,y : x._props["musicmoz"].set(y), fdel=None, doc=propDocs["musicmoz"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Performance(event___Event):
	"""
	mo:Performance
	
		A performance event. 
		It might include as agents performers, engineers, conductors, or even listeners.
		It might include as factors a score, a MusicalWork, musical instruments. 
		It might produce a sound:-)
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		event___Event.__init__(self)
		self._initialised = False
		self.shortname = "Performance"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["bpm"] = PropertySet("bpm","http://purl.org/ontology/mo/bpm", None, True)
		self._props["conductor"] = PropertySet("conductor","http://purl.org/ontology/mo/conductor", foaf___Agent, False)
		self._props["engineer"] = PropertySet("engineer","http://purl.org/ontology/mo/engineer", foaf___Agent, False)
		self._props["genre"] = PropertySet("genre","http://purl.org/ontology/mo/genre", (mo___Genre,rdfs___Resource), False)
		self._props["instrument"] = PropertySet("instrument","http://purl.org/ontology/mo/instrument", (rdfs___Resource,mo___Instrument), False)
		self._props["key"] = PropertySet("key","http://purl.org/ontology/mo/key", (rdfs___Resource,key___Key), False)
		self._props["listener"] = PropertySet("listener","http://purl.org/ontology/mo/listener", foaf___Agent, False)
		self._props["performance_of"] = PropertySet("performance_of","http://purl.org/ontology/mo/performance_of", (mo___MusicalWork,rdfs___Resource,mo___Score), False)
		self._props["performer"] = PropertySet("performer","http://purl.org/ontology/mo/performer", foaf___Agent, False)
		self._props["produced_sound"] = PropertySet("produced_sound","http://purl.org/ontology/mo/produced_sound", (rdfs___Resource,mo___Sound), False)
		self._props["recordedAs"] = PropertySet("recordedAs","http://purl.org/ontology/mo/recordedAs", None, False)
		self._props["recorded_as"] = PropertySet("recorded_as","http://purl.org/ontology/mo/recorded_as", mo___Signal, False)
		self._props["tempo"] = PropertySet("tempo","http://purl.org/ontology/mo/tempo", None, True)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Performance"


	# Python class properties to wrap the PropertySet objects
	bpm = property(fget=lambda x: x._props["bpm"].get(), fset=lambda x,y : x._props["bpm"].set(y), fdel=None, doc=propDocs["bpm"])
	conductor = property(fget=lambda x: x._props["conductor"].get(), fset=lambda x,y : x._props["conductor"].set(y), fdel=None, doc=propDocs["conductor"])
	engineer = property(fget=lambda x: x._props["engineer"].get(), fset=lambda x,y : x._props["engineer"].set(y), fdel=None, doc=propDocs["engineer"])
	genre = property(fget=lambda x: x._props["genre"].get(), fset=lambda x,y : x._props["genre"].set(y), fdel=None, doc=propDocs["genre"])
	instrument = property(fget=lambda x: x._props["instrument"].get(), fset=lambda x,y : x._props["instrument"].set(y), fdel=None, doc=propDocs["instrument"])
	key = property(fget=lambda x: x._props["key"].get(), fset=lambda x,y : x._props["key"].set(y), fdel=None, doc=propDocs["key"])
	listener = property(fget=lambda x: x._props["listener"].get(), fset=lambda x,y : x._props["listener"].set(y), fdel=None, doc=propDocs["listener"])
	performance_of = property(fget=lambda x: x._props["performance_of"].get(), fset=lambda x,y : x._props["performance_of"].set(y), fdel=None, doc=propDocs["performance_of"])
	performer = property(fget=lambda x: x._props["performer"].get(), fset=lambda x,y : x._props["performer"].set(y), fdel=None, doc=propDocs["performer"])
	produced_sound = property(fget=lambda x: x._props["produced_sound"].get(), fset=lambda x,y : x._props["produced_sound"].set(y), fdel=None, doc=propDocs["produced_sound"])
	recordedAs = property(fget=lambda x: x._props["recordedAs"].get(), fset=lambda x,y : x._props["recordedAs"].set(y), fdel=None, doc=propDocs["recordedAs"])
	recorded_as = property(fget=lambda x: x._props["recorded_as"].get(), fset=lambda x,y : x._props["recorded_as"].set(y), fdel=None, doc=propDocs["recorded_as"])
	tempo = property(fget=lambda x: x._props["tempo"].get(), fset=lambda x,y : x._props["tempo"].set(y), fdel=None, doc=propDocs["tempo"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___ReleaseStatus(rdfs___Resource):
	"""
	mo:ReleaseStatus
	Musical manifestation release status.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "ReleaseStatus"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/ReleaseStatus"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Score(mo___MusicalExpression):
	"""
	mo:Score
	
		Here, we are dealing with the informational object (the MusicalExpression), not the actually "published" score.
		This may be, for example, the product of an arrangement process.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicalExpression.__init__(self)
		self._initialised = False
		self.shortname = "Score"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["performed_in"] = PropertySet("performed_in","http://purl.org/ontology/mo/performed_in", (mo___Performance,event___Event), False)
		self._props["published_as"] = PropertySet("published_as","http://purl.org/ontology/mo/published_as", (mo___PublishedLibretto,mo___Record,mo___PublishedScore,mo___PublishedLyrics), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Score"


	# Python class properties to wrap the PropertySet objects
	performed_in = property(fget=lambda x: x._props["performed_in"].get(), fset=lambda x,y : x._props["performed_in"].set(y), fdel=None, doc=propDocs["performed_in"])
	published_as = property(fget=lambda x: x._props["published_as"].get(), fset=lambda x,y : x._props["published_as"].set(y), fdel=None, doc=propDocs["published_as"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Sound(event___Event, mo___MusicalExpression):
	"""
	mo:Sound
	
		A subclass of MusicalExpression, representing a sound. Realisation of a MusicalWork during a musical Performance.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		event___Event.__init__(self)
		mo___MusicalExpression.__init__(self)
		self._initialised = False
		self.shortname = "Sound"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["recorded_in"] = PropertySet("recorded_in","http://purl.org/ontology/mo/recorded_in", (mo___Recording,event___Event), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Sound"


	# Python class properties to wrap the PropertySet objects
	recorded_in = property(fget=lambda x: x._props["recorded_in"].get(), fset=lambda x,y : x._props["recorded_in"].set(y), fdel=None, doc=propDocs["recorded_in"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Stream(mo___Medium):
	"""
	mo:Stream
	Transmission over a network  used as medium to broadcast a musical manifestation
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "Stream"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Stream"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Vinyl(mo___Medium):
	"""
	mo:Vinyl
	Vinyl used as medium to record a musical manifestation
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "Vinyl"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Vinyl"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class frbr___Work(rdfs___Resource):
	"""
	frbr:Work
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Work"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["amazon_asin"] = PropertySet("amazon_asin","http://purl.org/ontology/mo/amazon_asin", foaf___Document, False)
		self._props["licence"] = PropertySet("licence","http://purl.org/ontology/mo/licence", foaf___Document, False)
		self._props["review"] = PropertySet("review","http://purl.org/ontology/mo/review", foaf___Document, False)
		self._props["wikipedia"] = PropertySet("wikipedia","http://purl.org/ontology/mo/wikipedia", foaf___Document, False)
		self._initialised = True
	classURI = "http://purl.org/vocab/frbr/core#Work"


	# Python class properties to wrap the PropertySet objects
	amazon_asin = property(fget=lambda x: x._props["amazon_asin"].get(), fset=lambda x,y : x._props["amazon_asin"].set(y), fdel=None, doc=propDocs["amazon_asin"])
	licence = property(fget=lambda x: x._props["licence"].get(), fset=lambda x,y : x._props["licence"].set(y), fdel=None, doc=propDocs["licence"])
	review = property(fget=lambda x: x._props["review"].get(), fset=lambda x,y : x._props["review"].set(y), fdel=None, doc=propDocs["review"])
	wikipedia = property(fget=lambda x: x._props["wikipedia"].get(), fset=lambda x,y : x._props["wikipedia"].set(y), fdel=None, doc=propDocs["wikipedia"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___DateTimeInterval(time___ProperInterval):
	"""
	time:DateTimeInterval
	"""
	def __init__(self,URI=None):
		# Initialise parents
		time___ProperInterval.__init__(self)
		self._initialised = False
		self.shortname = "DateTimeInterval"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hasDateTimeDescription"] = PropertySet("hasDateTimeDescription","http://www.w3.org/2006/time#hasDateTimeDescription", time___DateTimeDescription, False)
		self._props["xsdDateTime"] = PropertySet("xsdDateTime","http://www.w3.org/2006/time#xsdDateTime", str, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#DateTimeInterval"


	# Python class properties to wrap the PropertySet objects
	hasDateTimeDescription = property(fget=lambda x: x._props["hasDateTimeDescription"].get(), fset=lambda x,y : x._props["hasDateTimeDescription"].set(y), fdel=None, doc=propDocs["hasDateTimeDescription"])
	xsdDateTime = property(fget=lambda x: x._props["xsdDateTime"].get(), fset=lambda x,y : x._props["xsdDateTime"].set(y), fdel=None, doc=propDocs["xsdDateTime"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___January(time___DateTimeDescription):
	"""
	time:January
	"""
	def __init__(self,URI=None):
		# Initialise parents
		time___DateTimeDescription.__init__(self)
		self._initialised = False
		self.shortname = "January"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#January"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Agent(rdfs___Resource):
	"""
	foaf:Agent
	An agent (eg. person, group, software or physical artifact).
	
		An agent (person, group, software, etc.).
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Agent"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["isAgentIn"] = PropertySet("isAgentIn","http://purl.org/NET/c4dm/event.owl#isAgentIn", event___Event, False)
		self._props["collaborated_with"] = PropertySet("collaborated_with","http://purl.org/ontology/mo/collaborated_with", foaf___Agent, False)
		self._props["conducted"] = PropertySet("conducted","http://purl.org/ontology/mo/conducted", (mo___Performance,event___Event), False)
		self._props["download"] = PropertySet("download","http://purl.org/ontology/mo/download", foaf___Document, False)
		self._props["engineered"] = PropertySet("engineered","http://purl.org/ontology/mo/engineered", (mo___Recording,mo___Performance,event___Event), False)
		self._props["exchange_item"] = PropertySet("exchange_item","http://purl.org/ontology/mo/exchange_item", frbr___Item, False)
		self._props["free_download"] = PropertySet("free_download","http://purl.org/ontology/mo/free_download", foaf___Document, False)
		self._props["listened"] = PropertySet("listened","http://purl.org/ontology/mo/listened", (mo___Performance,event___Event), False)
		self._props["member_of"] = PropertySet("member_of","http://purl.org/ontology/mo/member_of", foaf___Group, False)
		self._props["musicbrainz"] = PropertySet("musicbrainz","http://purl.org/ontology/mo/musicbrainz", foaf___Document, False)
		self._props["myspace"] = PropertySet("myspace","http://purl.org/ontology/mo/myspace", foaf___Document, False)
		self._props["onlinecommunity"] = PropertySet("onlinecommunity","http://purl.org/ontology/mo/onlinecommunity", foaf___Document, False)
		self._props["paid_download"] = PropertySet("paid_download","http://purl.org/ontology/mo/paid_download", foaf___Document, False)
		self._props["performed"] = PropertySet("performed","http://purl.org/ontology/mo/performed", (mo___Performance,event___Event), False)
		self._props["possess_item"] = PropertySet("possess_item","http://purl.org/ontology/mo/possess_item", frbr___Item, False)
		self._props["preview_download"] = PropertySet("preview_download","http://purl.org/ontology/mo/preview_download", foaf___Document, False)
		self._props["produced"] = PropertySet("produced","http://purl.org/ontology/mo/produced", mo___MusicalManifestation, False)
		self._props["published"] = PropertySet("published","http://purl.org/ontology/mo/published", mo___MusicalManifestation, False)
		self._props["sell_item"] = PropertySet("sell_item","http://purl.org/ontology/mo/sell_item", frbr___Item, False)
		self._props["similar_to"] = PropertySet("similar_to","http://purl.org/ontology/mo/similar_to", (foaf___Agent,mo___Genre,mo___Signal), False)
		self._props["want_item"] = PropertySet("want_item","http://purl.org/ontology/mo/want_item", frbr___Item, False)
		self._props["wikipedia"] = PropertySet("wikipedia","http://purl.org/ontology/mo/wikipedia", foaf___Document, False)
		self._props["aimChatID"] = PropertySet("aimChatID","http://xmlns.com/foaf/0.1/aimChatID", None, True)
		self._props["birthday"] = PropertySet("birthday","http://xmlns.com/foaf/0.1/birthday", None, True)
		self._props["gender"] = PropertySet("gender","http://xmlns.com/foaf/0.1/gender", None, True)
		self._props["holdsAccount"] = PropertySet("holdsAccount","http://xmlns.com/foaf/0.1/holdsAccount", foaf___OnlineAccount, False)
		self._props["icqChatID"] = PropertySet("icqChatID","http://xmlns.com/foaf/0.1/icqChatID", None, True)
		self._props["jabberID"] = PropertySet("jabberID","http://xmlns.com/foaf/0.1/jabberID", None, True)
		self._props["made"] = PropertySet("made","http://xmlns.com/foaf/0.1/made", (mo___Track,owl___Thing,mo___MusicalManifestation,mo___Record), False)
		self._props["mbox"] = PropertySet("mbox","http://xmlns.com/foaf/0.1/mbox", owl___Thing, False)
		self._props["mbox_sha1sum"] = PropertySet("mbox_sha1sum","http://xmlns.com/foaf/0.1/mbox_sha1sum", None, True)
		self._props["msnChatID"] = PropertySet("msnChatID","http://xmlns.com/foaf/0.1/msnChatID", None, True)
		self._props["openid"] = PropertySet("openid","http://xmlns.com/foaf/0.1/openid", foaf___Document, False)
		self._props["tipjar"] = PropertySet("tipjar","http://xmlns.com/foaf/0.1/tipjar", foaf___Document, False)
		self._props["weblog"] = PropertySet("weblog","http://xmlns.com/foaf/0.1/weblog", foaf___Document, False)
		self._props["yahooChatID"] = PropertySet("yahooChatID","http://xmlns.com/foaf/0.1/yahooChatID", None, True)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Agent"


	# Python class properties to wrap the PropertySet objects
	isAgentIn = property(fget=lambda x: x._props["isAgentIn"].get(), fset=lambda x,y : x._props["isAgentIn"].set(y), fdel=None, doc=propDocs["isAgentIn"])
	collaborated_with = property(fget=lambda x: x._props["collaborated_with"].get(), fset=lambda x,y : x._props["collaborated_with"].set(y), fdel=None, doc=propDocs["collaborated_with"])
	conducted = property(fget=lambda x: x._props["conducted"].get(), fset=lambda x,y : x._props["conducted"].set(y), fdel=None, doc=propDocs["conducted"])
	download = property(fget=lambda x: x._props["download"].get(), fset=lambda x,y : x._props["download"].set(y), fdel=None, doc=propDocs["download"])
	engineered = property(fget=lambda x: x._props["engineered"].get(), fset=lambda x,y : x._props["engineered"].set(y), fdel=None, doc=propDocs["engineered"])
	exchange_item = property(fget=lambda x: x._props["exchange_item"].get(), fset=lambda x,y : x._props["exchange_item"].set(y), fdel=None, doc=propDocs["exchange_item"])
	free_download = property(fget=lambda x: x._props["free_download"].get(), fset=lambda x,y : x._props["free_download"].set(y), fdel=None, doc=propDocs["free_download"])
	listened = property(fget=lambda x: x._props["listened"].get(), fset=lambda x,y : x._props["listened"].set(y), fdel=None, doc=propDocs["listened"])
	member_of = property(fget=lambda x: x._props["member_of"].get(), fset=lambda x,y : x._props["member_of"].set(y), fdel=None, doc=propDocs["member_of"])
	musicbrainz = property(fget=lambda x: x._props["musicbrainz"].get(), fset=lambda x,y : x._props["musicbrainz"].set(y), fdel=None, doc=propDocs["musicbrainz"])
	myspace = property(fget=lambda x: x._props["myspace"].get(), fset=lambda x,y : x._props["myspace"].set(y), fdel=None, doc=propDocs["myspace"])
	onlinecommunity = property(fget=lambda x: x._props["onlinecommunity"].get(), fset=lambda x,y : x._props["onlinecommunity"].set(y), fdel=None, doc=propDocs["onlinecommunity"])
	paid_download = property(fget=lambda x: x._props["paid_download"].get(), fset=lambda x,y : x._props["paid_download"].set(y), fdel=None, doc=propDocs["paid_download"])
	performed = property(fget=lambda x: x._props["performed"].get(), fset=lambda x,y : x._props["performed"].set(y), fdel=None, doc=propDocs["performed"])
	possess_item = property(fget=lambda x: x._props["possess_item"].get(), fset=lambda x,y : x._props["possess_item"].set(y), fdel=None, doc=propDocs["possess_item"])
	preview_download = property(fget=lambda x: x._props["preview_download"].get(), fset=lambda x,y : x._props["preview_download"].set(y), fdel=None, doc=propDocs["preview_download"])
	produced = property(fget=lambda x: x._props["produced"].get(), fset=lambda x,y : x._props["produced"].set(y), fdel=None, doc=propDocs["produced"])
	published = property(fget=lambda x: x._props["published"].get(), fset=lambda x,y : x._props["published"].set(y), fdel=None, doc=propDocs["published"])
	sell_item = property(fget=lambda x: x._props["sell_item"].get(), fset=lambda x,y : x._props["sell_item"].set(y), fdel=None, doc=propDocs["sell_item"])
	similar_to = property(fget=lambda x: x._props["similar_to"].get(), fset=lambda x,y : x._props["similar_to"].set(y), fdel=None, doc=propDocs["similar_to"])
	want_item = property(fget=lambda x: x._props["want_item"].get(), fset=lambda x,y : x._props["want_item"].set(y), fdel=None, doc=propDocs["want_item"])
	wikipedia = property(fget=lambda x: x._props["wikipedia"].get(), fset=lambda x,y : x._props["wikipedia"].set(y), fdel=None, doc=propDocs["wikipedia"])
	aimChatID = property(fget=lambda x: x._props["aimChatID"].get(), fset=lambda x,y : x._props["aimChatID"].set(y), fdel=None, doc=propDocs["aimChatID"])
	birthday = property(fget=lambda x: x._props["birthday"].get(), fset=lambda x,y : x._props["birthday"].set(y), fdel=None, doc=propDocs["birthday"])
	gender = property(fget=lambda x: x._props["gender"].get(), fset=lambda x,y : x._props["gender"].set(y), fdel=None, doc=propDocs["gender"])
	holdsAccount = property(fget=lambda x: x._props["holdsAccount"].get(), fset=lambda x,y : x._props["holdsAccount"].set(y), fdel=None, doc=propDocs["holdsAccount"])
	icqChatID = property(fget=lambda x: x._props["icqChatID"].get(), fset=lambda x,y : x._props["icqChatID"].set(y), fdel=None, doc=propDocs["icqChatID"])
	jabberID = property(fget=lambda x: x._props["jabberID"].get(), fset=lambda x,y : x._props["jabberID"].set(y), fdel=None, doc=propDocs["jabberID"])
	made = property(fget=lambda x: x._props["made"].get(), fset=lambda x,y : x._props["made"].set(y), fdel=None, doc=propDocs["made"])
	mbox = property(fget=lambda x: x._props["mbox"].get(), fset=lambda x,y : x._props["mbox"].set(y), fdel=None, doc=propDocs["mbox"])
	mbox_sha1sum = property(fget=lambda x: x._props["mbox_sha1sum"].get(), fset=lambda x,y : x._props["mbox_sha1sum"].set(y), fdel=None, doc=propDocs["mbox_sha1sum"])
	msnChatID = property(fget=lambda x: x._props["msnChatID"].get(), fset=lambda x,y : x._props["msnChatID"].set(y), fdel=None, doc=propDocs["msnChatID"])
	openid = property(fget=lambda x: x._props["openid"].get(), fset=lambda x,y : x._props["openid"].set(y), fdel=None, doc=propDocs["openid"])
	tipjar = property(fget=lambda x: x._props["tipjar"].get(), fset=lambda x,y : x._props["tipjar"].set(y), fdel=None, doc=propDocs["tipjar"])
	weblog = property(fget=lambda x: x._props["weblog"].get(), fset=lambda x,y : x._props["weblog"].set(y), fdel=None, doc=propDocs["weblog"])
	yahooChatID = property(fget=lambda x: x._props["yahooChatID"].get(), fset=lambda x,y : x._props["yahooChatID"].set(y), fdel=None, doc=propDocs["yahooChatID"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Organization(foaf___Agent):
	"""
	foaf:Organization
	An organization.
	
		An organization.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Organization"
		self.URI = URI
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Organization"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class key___Key(rdfs___Resource):
	"""
	key:Key
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Key"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/keys.owl#Key"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___ContinuousTimeLine(timeline___TimeLine):
	"""
	timeline:ContinuousTimeLine
	A continuous timeline, like the universal one, or the one backing an analog signal
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___TimeLine.__init__(self)
		self._initialised = False
		self.shortname = "ContinuousTimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#ContinuousTimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___OriginMap(timeline___TimeLineMap):
	"""
	timeline:OriginMap
	
		This time line map represents the relation between the physical timeline and a
		continuous time line where the origin is at a given point on the physical timeline
		(eg. "the timeline backing this signal corresponds
		to the physical timeline: point 0 on this timeline corresponds to the
		20th of december at 5pm").
	
	A timeline map linking a physical timeline to a relative one (originating at some point on the physical timeline)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___TimeLineMap.__init__(self)
		self._initialised = False
		self.shortname = "OriginMap"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["origin"] = PropertySet("origin","http://purl.org/NET/c4dm/timeline.owl#origin", str, False)
		self._props["originAt"] = PropertySet("originAt","http://purl.org/NET/c4dm/timeline.owl#originAt", None, True)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#OriginMap"


	# Python class properties to wrap the PropertySet objects
	origin = property(fget=lambda x: x._props["origin"].get(), fset=lambda x,y : x._props["origin"].set(y), fdel=None, doc=propDocs["origin"])
	originAt = property(fget=lambda x: x._props["originAt"].get(), fset=lambda x,y : x._props["originAt"].set(y), fdel=None, doc=propDocs["originAt"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___RelativeTimeLine(timeline___ContinuousTimeLine, timeline___TimeLine):
	"""
	timeline:RelativeTimeLine
	
		A semi-infinite continuous timeline. Instances of RelativeTimeLine can
		back audio/video signals, sounds. Such timelines can
		be linked to a physical time line using the OriginMap.
	
	Semi infinite time line...canonical coordinate system --> adressed through xsd:duration since the instant 0.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___ContinuousTimeLine.__init__(self)
		timeline___TimeLine.__init__(self)
		self._initialised = False
		self.shortname = "RelativeTimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#RelativeTimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___UTInterval(rdfs___Resource):
	"""
	timeline:UTInterval
	an interval defined on the universal time line
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "UTInterval"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#UTInterval"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class chord___Interval(rdfs___Resource):
	"""
	chord:Interval
	An interval above the root of a chord.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Interval"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/chord/Interval"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class chord___SemitoneInterval(chord___Interval):
	"""
	chord:SemitoneInterval
	A semitone interval.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		chord___Interval.__init__(self)
		self._initialised = False
		self.shortname = "SemitoneInterval"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["semitone_interval"] = PropertySet("semitone_interval","http://purl.org/ontology/chord/semitone_interval", int, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/chord/SemitoneInterval"


	# Python class properties to wrap the PropertySet objects
	semitone_interval = property(fget=lambda x: x._props["semitone_interval"].get(), fset=lambda x,y : x._props["semitone_interval"].set(y), fdel=None, doc=propDocs["semitone_interval"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Arranger(foaf___Agent):
	"""
	mo:Arranger
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Arranger"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Arranger"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___CD(mo___Medium):
	"""
	mo:CD
	Compact Disc used as medium to record a musical manifestation.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "CD"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/CD"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Conductor(foaf___Agent):
	"""
	mo:Conductor
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Conductor"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Conductor"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___DAT(mo___Medium):
	"""
	mo:DAT
	Data Audio Tape used as medium to record a musical manifestation.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "DAT"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/DAT"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___DVDA(mo___Medium):
	"""
	mo:DVDA
	DVD-Audio used as medium to record a musical manifestation.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "DVDA"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/DVDA"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___ED2K(mo___Medium):
	"""
	mo:ED2K
	Something available on the E-Donkey peer-2-peer filesharing network
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "ED2K"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/ED2K"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Libretto(mo___MusicalExpression):
	"""
	mo:Libretto
	
                Libretto
        
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicalExpression.__init__(self)
		self._initialised = False
		self.shortname = "Libretto"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["published_as"] = PropertySet("published_as","http://purl.org/ontology/mo/published_as", (mo___PublishedLibretto,mo___Record,mo___PublishedScore,mo___PublishedLyrics), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Libretto"


	# Python class properties to wrap the PropertySet objects
	published_as = property(fget=lambda x: x._props["published_as"].get(), fset=lambda x,y : x._props["published_as"].set(y), fdel=None, doc=propDocs["published_as"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Lyrics(mo___MusicalExpression):
	"""
	mo:Lyrics
	
		Lyrics
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicalExpression.__init__(self)
		self._initialised = False
		self.shortname = "Lyrics"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["published_as"] = PropertySet("published_as","http://purl.org/ontology/mo/published_as", (mo___PublishedLibretto,mo___Record,mo___PublishedScore,mo___PublishedLyrics), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Lyrics"


	# Python class properties to wrap the PropertySet objects
	published_as = property(fget=lambda x: x._props["published_as"].get(), fset=lambda x,y : x._props["published_as"].set(y), fdel=None, doc=propDocs["published_as"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___MagneticTape(mo___Medium):
	"""
	mo:MagneticTape
	Magnetic analogue tape used as medium to record a musical manifestation.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "MagneticTape"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/MagneticTape"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___MusicArtist(foaf___Agent):
	"""
	mo:MusicArtist
	
		A person or a group of people (or a computer :-) ), whose musical 
		creative work shows sensitivity and imagination 
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "MusicArtist"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["biography"] = PropertySet("biography","http://purl.org/ontology/mo/biography", foaf___Document, False)
		self._props["compiled"] = PropertySet("compiled","http://purl.org/ontology/mo/compiled", mo___MusicalManifestation, False)
		self._props["discography"] = PropertySet("discography","http://purl.org/ontology/mo/discography", foaf___Document, False)
		self._props["discogs"] = PropertySet("discogs","http://purl.org/ontology/mo/discogs", foaf___Document, False)
		self._props["djmixed"] = PropertySet("djmixed","http://purl.org/ontology/mo/djmixed", mo___Signal, False)
		self._props["fanpage"] = PropertySet("fanpage","http://purl.org/ontology/mo/fanpage", foaf___Document, False)
		self._props["imdb"] = PropertySet("imdb","http://purl.org/ontology/mo/imdb", foaf___Document, False)
		self._props["mailorder"] = PropertySet("mailorder","http://purl.org/ontology/mo/mailorder", foaf___Document, False)
		self._props["musicmoz"] = PropertySet("musicmoz","http://purl.org/ontology/mo/musicmoz", foaf___Document, False)
		self._props["paid_download"] = PropertySet("paid_download","http://purl.org/ontology/mo/paid_download", foaf___Document, False)
		self._props["remixed"] = PropertySet("remixed","http://purl.org/ontology/mo/remixed", mo___Signal, False)
		self._props["sampled"] = PropertySet("sampled","http://purl.org/ontology/mo/sampled", mo___Signal, False)
		self._props["supporting_musician"] = PropertySet("supporting_musician","http://purl.org/ontology/mo/supporting_musician", mo___MusicArtist, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/MusicArtist"


	# Python class properties to wrap the PropertySet objects
	biography = property(fget=lambda x: x._props["biography"].get(), fset=lambda x,y : x._props["biography"].set(y), fdel=None, doc=propDocs["biography"])
	compiled = property(fget=lambda x: x._props["compiled"].get(), fset=lambda x,y : x._props["compiled"].set(y), fdel=None, doc=propDocs["compiled"])
	discography = property(fget=lambda x: x._props["discography"].get(), fset=lambda x,y : x._props["discography"].set(y), fdel=None, doc=propDocs["discography"])
	discogs = property(fget=lambda x: x._props["discogs"].get(), fset=lambda x,y : x._props["discogs"].set(y), fdel=None, doc=propDocs["discogs"])
	djmixed = property(fget=lambda x: x._props["djmixed"].get(), fset=lambda x,y : x._props["djmixed"].set(y), fdel=None, doc=propDocs["djmixed"])
	fanpage = property(fget=lambda x: x._props["fanpage"].get(), fset=lambda x,y : x._props["fanpage"].set(y), fdel=None, doc=propDocs["fanpage"])
	imdb = property(fget=lambda x: x._props["imdb"].get(), fset=lambda x,y : x._props["imdb"].set(y), fdel=None, doc=propDocs["imdb"])
	mailorder = property(fget=lambda x: x._props["mailorder"].get(), fset=lambda x,y : x._props["mailorder"].set(y), fdel=None, doc=propDocs["mailorder"])
	musicmoz = property(fget=lambda x: x._props["musicmoz"].get(), fset=lambda x,y : x._props["musicmoz"].set(y), fdel=None, doc=propDocs["musicmoz"])
	paid_download = property(fget=lambda x: x._props["paid_download"].get(), fset=lambda x,y : x._props["paid_download"].set(y), fdel=None, doc=propDocs["paid_download"])
	remixed = property(fget=lambda x: x._props["remixed"].get(), fset=lambda x,y : x._props["remixed"].set(y), fdel=None, doc=propDocs["remixed"])
	sampled = property(fget=lambda x: x._props["sampled"].get(), fset=lambda x,y : x._props["sampled"].set(y), fdel=None, doc=propDocs["sampled"])
	supporting_musician = property(fget=lambda x: x._props["supporting_musician"].get(), fset=lambda x,y : x._props["supporting_musician"].set(y), fdel=None, doc=propDocs["supporting_musician"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___MusicalManifestation(frbr___Manifestation):
	"""
	mo:MusicalManifestation
	

This entity is related to the edition/production/publication of a musical expression (musical manifestation are closely related with the music industry (their terms, concepts, definitions, methods (production, publication, etc.), etc.)
    
From the FRBR final report: The entity defined as manifestation encompasses a wide range of materials, including manuscripts, books, periodicals, maps, posters, sound recordings, films, video recordings, CD-ROMs, multimedia kits, etc. As an entity, manifestation represents all the physical objects that bear the same characteristics, in respect to both intellectual content and physical form.


Work #1 J. S. Bach's Six suites for unaccompanied cello

    * Expression #1 sound issued during the performance by Janos Starker recorded in 1963 and 1965
          o Manifestation #1 recordings released on 33 1/3 rpm sound discs in 1965 by Mercury
          o Manifestation #2 recordings re-released on compact disc in 1991 by Mercury 
    * Expression #2 sound issued during the performances by Yo-Yo Ma recorded in 1983
          o Manifestation #1 recordings released on 33 1/3 rpm sound discs in 1983 by CBS Records
          o Manifestation #2 recordings re-released on compact disc in 1992 by CBS Records 

          
Changes that occur deliberately or even inadvertently in the production process that affect the copies result, strictly speaking, in a new manifestation. A manifestation resulting from such a change may be identified as a particular "state" or "issue" of the publication.

Changes that occur to an individual copy after the production process is complete (e.g., the loss of a page, rebinding, etc.) are not considered to result in a new manifestation. That copy is simply considered to be an exemplar (or item) of the manifestation that deviates from the copy as produced.

With the entity defined as manifestation we can describe the physical characteristics of a set of items and the characteristics associated with the production and distribution of that set of items that may be important factors in enabling users to choose a manifestation appropriate to their physical needs and constraints, and to identify and acquire a copy of that manifestation.

Defining manifestation as an entity also enables us to draw relationships between specific manifestations of a work. We can use the relationships between manifestations to identify, for example, the specific publication that was used to create a microreproduction.          


	"""
	def __init__(self,URI=None):
		# Initialise parents
		frbr___Manifestation.__init__(self)
		self._initialised = False
		self.shortname = "MusicalManifestation"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["available_as"] = PropertySet("available_as","http://purl.org/ontology/mo/available_as", mo___MusicalItem, False)
		self._props["compilation_of"] = PropertySet("compilation_of","http://purl.org/ontology/mo/compilation_of", mo___Signal, False)
		self._props["compiler"] = PropertySet("compiler","http://purl.org/ontology/mo/compiler", mo___MusicArtist, False)
		self._props["discogs"] = PropertySet("discogs","http://purl.org/ontology/mo/discogs", foaf___Document, False)
		self._props["image"] = PropertySet("image","http://purl.org/ontology/mo/image", (foaf___Image,rdfs___Resource), False)
		self._props["imdb"] = PropertySet("imdb","http://purl.org/ontology/mo/imdb", foaf___Document, False)
		self._props["item"] = PropertySet("item","http://purl.org/ontology/mo/item", mo___MusicalItem, False)
		self._props["musicbrainz"] = PropertySet("musicbrainz","http://purl.org/ontology/mo/musicbrainz", foaf___Document, False)
		self._props["musicmoz"] = PropertySet("musicmoz","http://purl.org/ontology/mo/musicmoz", foaf___Document, False)
		self._props["other_release_of"] = PropertySet("other_release_of","http://purl.org/ontology/mo/other_release_of", mo___MusicalManifestation, False)
		self._props["preview"] = PropertySet("preview","http://purl.org/ontology/mo/preview", mo___MusicalItem, False)
		self._props["producer"] = PropertySet("producer","http://purl.org/ontology/mo/producer", foaf___Agent, False)
		self._props["publisher"] = PropertySet("publisher","http://purl.org/ontology/mo/publisher", foaf___Agent, False)
		self._props["publishing_location"] = PropertySet("publishing_location","http://purl.org/ontology/mo/publishing_location", geo___SpatialThing, False)
		self._props["release_status"] = PropertySet("release_status","http://purl.org/ontology/mo/release_status", mo___ReleaseStatus, False)
		self._props["release_type"] = PropertySet("release_type","http://purl.org/ontology/mo/release_type", mo___ReleaseType, False)
		self._props["tribute_to"] = PropertySet("tribute_to","http://purl.org/ontology/mo/tribute_to", mo___MusicArtist, False)
		self._props["maker"] = PropertySet("maker","http://xmlns.com/foaf/0.1/maker", foaf___Agent, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/MusicalManifestation"


	# Python class properties to wrap the PropertySet objects
	available_as = property(fget=lambda x: x._props["available_as"].get(), fset=lambda x,y : x._props["available_as"].set(y), fdel=None, doc=propDocs["available_as"])
	compilation_of = property(fget=lambda x: x._props["compilation_of"].get(), fset=lambda x,y : x._props["compilation_of"].set(y), fdel=None, doc=propDocs["compilation_of"])
	compiler = property(fget=lambda x: x._props["compiler"].get(), fset=lambda x,y : x._props["compiler"].set(y), fdel=None, doc=propDocs["compiler"])
	discogs = property(fget=lambda x: x._props["discogs"].get(), fset=lambda x,y : x._props["discogs"].set(y), fdel=None, doc=propDocs["discogs"])
	image = property(fget=lambda x: x._props["image"].get(), fset=lambda x,y : x._props["image"].set(y), fdel=None, doc=propDocs["image"])
	imdb = property(fget=lambda x: x._props["imdb"].get(), fset=lambda x,y : x._props["imdb"].set(y), fdel=None, doc=propDocs["imdb"])
	item = property(fget=lambda x: x._props["item"].get(), fset=lambda x,y : x._props["item"].set(y), fdel=None, doc=propDocs["item"])
	musicbrainz = property(fget=lambda x: x._props["musicbrainz"].get(), fset=lambda x,y : x._props["musicbrainz"].set(y), fdel=None, doc=propDocs["musicbrainz"])
	musicmoz = property(fget=lambda x: x._props["musicmoz"].get(), fset=lambda x,y : x._props["musicmoz"].set(y), fdel=None, doc=propDocs["musicmoz"])
	other_release_of = property(fget=lambda x: x._props["other_release_of"].get(), fset=lambda x,y : x._props["other_release_of"].set(y), fdel=None, doc=propDocs["other_release_of"])
	preview = property(fget=lambda x: x._props["preview"].get(), fset=lambda x,y : x._props["preview"].set(y), fdel=None, doc=propDocs["preview"])
	producer = property(fget=lambda x: x._props["producer"].get(), fset=lambda x,y : x._props["producer"].set(y), fdel=None, doc=propDocs["producer"])
	publisher = property(fget=lambda x: x._props["publisher"].get(), fset=lambda x,y : x._props["publisher"].set(y), fdel=None, doc=propDocs["publisher"])
	publishing_location = property(fget=lambda x: x._props["publishing_location"].get(), fset=lambda x,y : x._props["publishing_location"].set(y), fdel=None, doc=propDocs["publishing_location"])
	release_status = property(fget=lambda x: x._props["release_status"].get(), fset=lambda x,y : x._props["release_status"].set(y), fdel=None, doc=propDocs["release_status"])
	release_type = property(fget=lambda x: x._props["release_type"].get(), fset=lambda x,y : x._props["release_type"].set(y), fdel=None, doc=propDocs["release_type"])
	tribute_to = property(fget=lambda x: x._props["tribute_to"].get(), fset=lambda x,y : x._props["tribute_to"].set(y), fdel=None, doc=propDocs["tribute_to"])
	maker = property(fget=lambda x: x._props["maker"].get(), fset=lambda x,y : x._props["maker"].set(y), fdel=None, doc=propDocs["maker"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Performer(foaf___Agent):
	"""
	mo:Performer
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Performer"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Performer"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___PublishedLyrics(mo___MusicalManifestation):
	"""
	mo:PublishedLyrics
	Published lyrics, as a book or as a text file, for example
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicalManifestation.__init__(self)
		self._initialised = False
		self.shortname = "PublishedLyrics"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["publication_of"] = PropertySet("publication_of","http://purl.org/ontology/mo/publication_of", (mo___Signal,mo___Libretto,mo___Lyrics,mo___Score), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/PublishedLyrics"


	# Python class properties to wrap the PropertySet objects
	publication_of = property(fget=lambda x: x._props["publication_of"].get(), fset=lambda x,y : x._props["publication_of"].set(y), fdel=None, doc=propDocs["publication_of"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Record(mo___MusicalManifestation):
	"""
	mo:Record
	A published record (manifestation which first aim is to render the product of a recording)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicalManifestation.__init__(self)
		self._initialised = False
		self.shortname = "Record"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["publication_of"] = PropertySet("publication_of","http://purl.org/ontology/mo/publication_of", (mo___Signal,mo___Libretto,mo___Lyrics,mo___Score), False)
		self._props["track"] = PropertySet("track","http://purl.org/ontology/mo/track", mo___Track, False)
		self._props["maker"] = PropertySet("maker","http://xmlns.com/foaf/0.1/maker", foaf___Agent, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Record"


	# Python class properties to wrap the PropertySet objects
	publication_of = property(fget=lambda x: x._props["publication_of"].get(), fset=lambda x,y : x._props["publication_of"].set(y), fdel=None, doc=propDocs["publication_of"])
	track = property(fget=lambda x: x._props["track"].get(), fset=lambda x,y : x._props["track"].set(y), fdel=None, doc=propDocs["track"])
	maker = property(fget=lambda x: x._props["maker"].get(), fset=lambda x,y : x._props["maker"].set(y), fdel=None, doc=propDocs["maker"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Signal(mo___MusicalExpression):
	"""
	mo:Signal
	
		A subclass of MusicalExpression, representing a Signal. Realisation of a MusicalWork through both a Performance and a Recording.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicalExpression.__init__(self)
		self._initialised = False
		self.shortname = "Signal"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["channels"] = PropertySet("channels","http://purl.org/ontology/mo/channels", None, True)
		self._props["contains_sample_from"] = PropertySet("contains_sample_from","http://purl.org/ontology/mo/contains_sample_from", mo___Signal, False)
		self._props["djmix_of"] = PropertySet("djmix_of","http://purl.org/ontology/mo/djmix_of", mo___Signal, False)
		self._props["djmixed_by"] = PropertySet("djmixed_by","http://purl.org/ontology/mo/djmixed_by", mo___MusicArtist, False)
		self._props["isrc"] = PropertySet("isrc","http://purl.org/ontology/mo/isrc", None, True)
		self._props["mashup_of"] = PropertySet("mashup_of","http://purl.org/ontology/mo/mashup_of", mo___Signal, False)
		self._props["medley_of"] = PropertySet("medley_of","http://purl.org/ontology/mo/medley_of", mo___Signal, False)
		self._props["musicbrainz"] = PropertySet("musicbrainz","http://purl.org/ontology/mo/musicbrainz", foaf___Document, False)
		self._props["published_as"] = PropertySet("published_as","http://purl.org/ontology/mo/published_as", (mo___PublishedLibretto,mo___Record,mo___PublishedScore,mo___PublishedLyrics), False)
		self._props["puid"] = PropertySet("puid","http://purl.org/ontology/mo/puid", None, True)
		self._props["records"] = PropertySet("records","http://purl.org/ontology/mo/records", mo___Performance, False)
		self._props["remaster_of"] = PropertySet("remaster_of","http://purl.org/ontology/mo/remaster_of", mo___Signal, False)
		self._props["remix_of"] = PropertySet("remix_of","http://purl.org/ontology/mo/remix_of", mo___Signal, False)
		self._props["remixer"] = PropertySet("remixer","http://purl.org/ontology/mo/remixer", mo___MusicArtist, False)
		self._props["sampler"] = PropertySet("sampler","http://purl.org/ontology/mo/sampler", mo___MusicArtist, False)
		self._props["similar_to"] = PropertySet("similar_to","http://purl.org/ontology/mo/similar_to", (foaf___Agent,mo___Genre,mo___Signal), False)
		self._props["time"] = PropertySet("time","http://purl.org/ontology/mo/time", time___TemporalEntity, False)
		self._props["trmid"] = PropertySet("trmid","http://purl.org/ontology/mo/trmid", None, True)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Signal"


	# Python class properties to wrap the PropertySet objects
	channels = property(fget=lambda x: x._props["channels"].get(), fset=lambda x,y : x._props["channels"].set(y), fdel=None, doc=propDocs["channels"])
	contains_sample_from = property(fget=lambda x: x._props["contains_sample_from"].get(), fset=lambda x,y : x._props["contains_sample_from"].set(y), fdel=None, doc=propDocs["contains_sample_from"])
	djmix_of = property(fget=lambda x: x._props["djmix_of"].get(), fset=lambda x,y : x._props["djmix_of"].set(y), fdel=None, doc=propDocs["djmix_of"])
	djmixed_by = property(fget=lambda x: x._props["djmixed_by"].get(), fset=lambda x,y : x._props["djmixed_by"].set(y), fdel=None, doc=propDocs["djmixed_by"])
	isrc = property(fget=lambda x: x._props["isrc"].get(), fset=lambda x,y : x._props["isrc"].set(y), fdel=None, doc=propDocs["isrc"])
	mashup_of = property(fget=lambda x: x._props["mashup_of"].get(), fset=lambda x,y : x._props["mashup_of"].set(y), fdel=None, doc=propDocs["mashup_of"])
	medley_of = property(fget=lambda x: x._props["medley_of"].get(), fset=lambda x,y : x._props["medley_of"].set(y), fdel=None, doc=propDocs["medley_of"])
	musicbrainz = property(fget=lambda x: x._props["musicbrainz"].get(), fset=lambda x,y : x._props["musicbrainz"].set(y), fdel=None, doc=propDocs["musicbrainz"])
	published_as = property(fget=lambda x: x._props["published_as"].get(), fset=lambda x,y : x._props["published_as"].set(y), fdel=None, doc=propDocs["published_as"])
	puid = property(fget=lambda x: x._props["puid"].get(), fset=lambda x,y : x._props["puid"].set(y), fdel=None, doc=propDocs["puid"])
	records = property(fget=lambda x: x._props["records"].get(), fset=lambda x,y : x._props["records"].set(y), fdel=None, doc=propDocs["records"])
	remaster_of = property(fget=lambda x: x._props["remaster_of"].get(), fset=lambda x,y : x._props["remaster_of"].set(y), fdel=None, doc=propDocs["remaster_of"])
	remix_of = property(fget=lambda x: x._props["remix_of"].get(), fset=lambda x,y : x._props["remix_of"].set(y), fdel=None, doc=propDocs["remix_of"])
	remixer = property(fget=lambda x: x._props["remixer"].get(), fset=lambda x,y : x._props["remixer"].set(y), fdel=None, doc=propDocs["remixer"])
	sampler = property(fget=lambda x: x._props["sampler"].get(), fset=lambda x,y : x._props["sampler"].set(y), fdel=None, doc=propDocs["sampler"])
	similar_to = property(fget=lambda x: x._props["similar_to"].get(), fset=lambda x,y : x._props["similar_to"].set(y), fdel=None, doc=propDocs["similar_to"])
	time = property(fget=lambda x: x._props["time"].get(), fset=lambda x,y : x._props["time"].set(y), fdel=None, doc=propDocs["time"])
	trmid = property(fget=lambda x: x._props["trmid"].get(), fset=lambda x,y : x._props["trmid"].set(y), fdel=None, doc=propDocs["trmid"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___SoundEngineer(foaf___Agent):
	"""
	mo:SoundEngineer
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "SoundEngineer"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/SoundEngineer"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Track(mo___Record):
	"""
	mo:Track
	A track on a particular record
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Record.__init__(self)
		self._initialised = False
		self.shortname = "Track"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["olga"] = PropertySet("olga","http://purl.org/ontology/mo/olga", foaf___Document, False)
		self._props["track_number"] = PropertySet("track_number","http://purl.org/ontology/mo/track_number", None, True)
		self._props["maker"] = PropertySet("maker","http://xmlns.com/foaf/0.1/maker", foaf___Agent, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Track"


	# Python class properties to wrap the PropertySet objects
	olga = property(fget=lambda x: x._props["olga"].get(), fset=lambda x,y : x._props["olga"].set(y), fdel=None, doc=propDocs["olga"])
	track_number = property(fget=lambda x: x._props["track_number"].get(), fset=lambda x,y : x._props["track_number"].set(y), fdel=None, doc=propDocs["track_number"])
	maker = property(fget=lambda x: x._props["maker"].get(), fset=lambda x,y : x._props["maker"].set(y), fdel=None, doc=propDocs["maker"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class owl___Nothing(rdfs___Resource):
	"""
	owl:Nothing
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Nothing"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2002/07/owl#Nothing"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___TemporalUnit(rdfs___Resource):
	"""
	time:TemporalUnit
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "TemporalUnit"
		self.URI = URI
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#TemporalUnit"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Person(foaf___Agent, geo___SpatialThing):
	"""
	foaf:Person
	A person.
	
		A person.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		geo___SpatialThing.__init__(self)
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Person"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["member_of"] = PropertySet("member_of","http://purl.org/ontology/mo/member_of", foaf___Group, False)
		self._props["currentProject"] = PropertySet("currentProject","http://xmlns.com/foaf/0.1/currentProject", owl___Thing, False)
		self._props["family_name"] = PropertySet("family_name","http://xmlns.com/foaf/0.1/family_name", None, True)
		self._props["firstName"] = PropertySet("firstName","http://xmlns.com/foaf/0.1/firstName", None, True)
		self._props["geekcode"] = PropertySet("geekcode","http://xmlns.com/foaf/0.1/geekcode", None, True)
		self._props["img"] = PropertySet("img","http://xmlns.com/foaf/0.1/img", foaf___Image, False)
		self._props["interest"] = PropertySet("interest","http://xmlns.com/foaf/0.1/interest", foaf___Document, False)
		self._props["knows"] = PropertySet("knows","http://xmlns.com/foaf/0.1/knows", foaf___Person, False)
		self._props["myersBriggs"] = PropertySet("myersBriggs","http://xmlns.com/foaf/0.1/myersBriggs", None, True)
		self._props["pastProject"] = PropertySet("pastProject","http://xmlns.com/foaf/0.1/pastProject", owl___Thing, False)
		self._props["plan"] = PropertySet("plan","http://xmlns.com/foaf/0.1/plan", None, True)
		self._props["publications"] = PropertySet("publications","http://xmlns.com/foaf/0.1/publications", foaf___Document, False)
		self._props["schoolHomepage"] = PropertySet("schoolHomepage","http://xmlns.com/foaf/0.1/schoolHomepage", foaf___Document, False)
		self._props["surname"] = PropertySet("surname","http://xmlns.com/foaf/0.1/surname", None, True)
		self._props["topic_interest"] = PropertySet("topic_interest","http://xmlns.com/foaf/0.1/topic_interest", owl___Thing, False)
		self._props["workInfoHomepage"] = PropertySet("workInfoHomepage","http://xmlns.com/foaf/0.1/workInfoHomepage", foaf___Document, False)
		self._props["workplaceHomepage"] = PropertySet("workplaceHomepage","http://xmlns.com/foaf/0.1/workplaceHomepage", foaf___Document, False)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Person"


	# Python class properties to wrap the PropertySet objects
	member_of = property(fget=lambda x: x._props["member_of"].get(), fset=lambda x,y : x._props["member_of"].set(y), fdel=None, doc=propDocs["member_of"])
	currentProject = property(fget=lambda x: x._props["currentProject"].get(), fset=lambda x,y : x._props["currentProject"].set(y), fdel=None, doc=propDocs["currentProject"])
	family_name = property(fget=lambda x: x._props["family_name"].get(), fset=lambda x,y : x._props["family_name"].set(y), fdel=None, doc=propDocs["family_name"])
	firstName = property(fget=lambda x: x._props["firstName"].get(), fset=lambda x,y : x._props["firstName"].set(y), fdel=None, doc=propDocs["firstName"])
	geekcode = property(fget=lambda x: x._props["geekcode"].get(), fset=lambda x,y : x._props["geekcode"].set(y), fdel=None, doc=propDocs["geekcode"])
	img = property(fget=lambda x: x._props["img"].get(), fset=lambda x,y : x._props["img"].set(y), fdel=None, doc=propDocs["img"])
	interest = property(fget=lambda x: x._props["interest"].get(), fset=lambda x,y : x._props["interest"].set(y), fdel=None, doc=propDocs["interest"])
	knows = property(fget=lambda x: x._props["knows"].get(), fset=lambda x,y : x._props["knows"].set(y), fdel=None, doc=propDocs["knows"])
	myersBriggs = property(fget=lambda x: x._props["myersBriggs"].get(), fset=lambda x,y : x._props["myersBriggs"].set(y), fdel=None, doc=propDocs["myersBriggs"])
	pastProject = property(fget=lambda x: x._props["pastProject"].get(), fset=lambda x,y : x._props["pastProject"].set(y), fdel=None, doc=propDocs["pastProject"])
	plan = property(fget=lambda x: x._props["plan"].get(), fset=lambda x,y : x._props["plan"].set(y), fdel=None, doc=propDocs["plan"])
	publications = property(fget=lambda x: x._props["publications"].get(), fset=lambda x,y : x._props["publications"].set(y), fdel=None, doc=propDocs["publications"])
	schoolHomepage = property(fget=lambda x: x._props["schoolHomepage"].get(), fset=lambda x,y : x._props["schoolHomepage"].set(y), fdel=None, doc=propDocs["schoolHomepage"])
	surname = property(fget=lambda x: x._props["surname"].get(), fset=lambda x,y : x._props["surname"].set(y), fdel=None, doc=propDocs["surname"])
	topic_interest = property(fget=lambda x: x._props["topic_interest"].get(), fset=lambda x,y : x._props["topic_interest"].set(y), fdel=None, doc=propDocs["topic_interest"])
	workInfoHomepage = property(fget=lambda x: x._props["workInfoHomepage"].get(), fset=lambda x,y : x._props["workInfoHomepage"].set(y), fdel=None, doc=propDocs["workInfoHomepage"])
	workplaceHomepage = property(fget=lambda x: x._props["workplaceHomepage"].get(), fset=lambda x,y : x._props["workplaceHomepage"].set(y), fdel=None, doc=propDocs["workplaceHomepage"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___AbstractInterval(timeline___Interval):
	"""
	timeline:AbstractInterval
	
	An interval defined on an abstract time-line.
    
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___Interval.__init__(self)
		self._initialised = False
		self.shortname = "AbstractInterval"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#AbstractInterval"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___PhysicalTimeLine(timeline___ContinuousTimeLine, timeline___TimeLine):
	"""
	timeline:PhysicalTimeLine
	
		Well, the actual physical time as we know it. I may want to address "yesterday" on instances
		of this class, or "the year 1789"...
	
	A "physical" time-line (the universal time line (UTC)) is an instance of this class. Other time zones consists in instances of this class as well, with a "shifting" time line map relating them to the universal time line map.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___ContinuousTimeLine.__init__(self)
		timeline___TimeLine.__init__(self)
		self._initialised = False
		self.shortname = "PhysicalTimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#PhysicalTimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___UniformWindowingMap(timeline___TimeLineMap):
	"""
	timeline:UniformWindowingMap
	Describes the relation between a discrete time line and its windowed equivalent
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___TimeLineMap.__init__(self)
		self._initialised = False
		self.shortname = "UniformWindowingMap"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["hopSize"] = PropertySet("hopSize","http://purl.org/NET/c4dm/timeline.owl#hopSize", int, False)
		self._props["windowLength"] = PropertySet("windowLength","http://purl.org/NET/c4dm/timeline.owl#windowLength", int, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#UniformWindowingMap"


	# Python class properties to wrap the PropertySet objects
	hopSize = property(fget=lambda x: x._props["hopSize"].get(), fset=lambda x,y : x._props["hopSize"].set(y), fdel=None, doc=propDocs["hopSize"])
	windowLength = property(fget=lambda x: x._props["windowLength"].get(), fset=lambda x,y : x._props["windowLength"].set(y), fdel=None, doc=propDocs["windowLength"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___AnalogSignal(mo___Signal):
	"""
	mo:AnalogSignal
	
		An analog signal.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Signal.__init__(self)
		self._initialised = False
		self.shortname = "AnalogSignal"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["sampled_version"] = PropertySet("sampled_version","http://purl.org/ontology/mo/sampled_version", mo___DigitalSignal, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/AnalogSignal"


	# Python class properties to wrap the PropertySet objects
	sampled_version = property(fget=lambda x: x._props["sampled_version"].get(), fset=lambda x,y : x._props["sampled_version"].set(y), fdel=None, doc=propDocs["sampled_version"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Composer(foaf___Agent):
	"""
	mo:Composer
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Composer"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Composer"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___DCC(mo___Medium):
	"""
	mo:DCC
	Digital Compact Cassette used as medium to record a musical manifestation.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "DCC"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/DCC"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Instrumentation(mo___Arrangement):
	"""
	mo:Instrumentation
	
		Instrumentation deals with the techniques of writing music for a specific instrument, 
		including the limitations of the instrument, playing techniques and idiomatic handling of the instrument.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Arrangement.__init__(self)
		self._initialised = False
		self.shortname = "Instrumentation"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Instrumentation"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Listener(foaf___Agent):
	"""
	mo:Listener
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Listener"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Listener"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___MusicalWork(frbr___Work):
	"""
	mo:MusicalWork
	
	Distinct intellectual or artistic musical creation.
    
From the FRBR final report: A work is an abstract entity; there is no single material object one can point to as the work. We recognize the work through individual realizations or expressions of the work, but the work itself exists only in the commonality of
content between and among the various expressions of the work. When we speak of Homer's Iliad as a work, our point of reference is not a particular recitation or text of the work, but the intellectual creation that lies behind all the various expressions of the work.     

For example:

work #1 J. S. Bach's The art of the fugue

    
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		frbr___Work.__init__(self)
		self._initialised = False
		self.shortname = "MusicalWork"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["arranged_in"] = PropertySet("arranged_in","http://purl.org/ontology/mo/arranged_in", (mo___Arrangement,event___Event), False)
		self._props["bpm"] = PropertySet("bpm","http://purl.org/ontology/mo/bpm", None, True)
		self._props["composed_in"] = PropertySet("composed_in","http://purl.org/ontology/mo/composed_in", (mo___Composition,event___Event), False)
		self._props["discogs"] = PropertySet("discogs","http://purl.org/ontology/mo/discogs", foaf___Document, False)
		self._props["has_movement"] = PropertySet("has_movement","http://purl.org/ontology/mo/has_movement", mo___Movement, False)
		self._props["image"] = PropertySet("image","http://purl.org/ontology/mo/image", (foaf___Image,rdfs___Resource), False)
		self._props["imdb"] = PropertySet("imdb","http://purl.org/ontology/mo/imdb", foaf___Document, False)
		self._props["key"] = PropertySet("key","http://purl.org/ontology/mo/key", (rdfs___Resource,key___Key), False)
		self._props["musicbrainz"] = PropertySet("musicbrainz","http://purl.org/ontology/mo/musicbrainz", foaf___Document, False)
		self._props["musicmoz"] = PropertySet("musicmoz","http://purl.org/ontology/mo/musicmoz", foaf___Document, False)
		self._props["opus"] = PropertySet("opus","http://purl.org/ontology/mo/opus", None, True)
		self._props["performed_in"] = PropertySet("performed_in","http://purl.org/ontology/mo/performed_in", (mo___Performance,event___Event), False)
		self._props["tempo"] = PropertySet("tempo","http://purl.org/ontology/mo/tempo", None, True)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/MusicalWork"


	# Python class properties to wrap the PropertySet objects
	arranged_in = property(fget=lambda x: x._props["arranged_in"].get(), fset=lambda x,y : x._props["arranged_in"].set(y), fdel=None, doc=propDocs["arranged_in"])
	bpm = property(fget=lambda x: x._props["bpm"].get(), fset=lambda x,y : x._props["bpm"].set(y), fdel=None, doc=propDocs["bpm"])
	composed_in = property(fget=lambda x: x._props["composed_in"].get(), fset=lambda x,y : x._props["composed_in"].set(y), fdel=None, doc=propDocs["composed_in"])
	discogs = property(fget=lambda x: x._props["discogs"].get(), fset=lambda x,y : x._props["discogs"].set(y), fdel=None, doc=propDocs["discogs"])
	has_movement = property(fget=lambda x: x._props["has_movement"].get(), fset=lambda x,y : x._props["has_movement"].set(y), fdel=None, doc=propDocs["has_movement"])
	image = property(fget=lambda x: x._props["image"].get(), fset=lambda x,y : x._props["image"].set(y), fdel=None, doc=propDocs["image"])
	imdb = property(fget=lambda x: x._props["imdb"].get(), fset=lambda x,y : x._props["imdb"].set(y), fdel=None, doc=propDocs["imdb"])
	key = property(fget=lambda x: x._props["key"].get(), fset=lambda x,y : x._props["key"].set(y), fdel=None, doc=propDocs["key"])
	musicbrainz = property(fget=lambda x: x._props["musicbrainz"].get(), fset=lambda x,y : x._props["musicbrainz"].set(y), fdel=None, doc=propDocs["musicbrainz"])
	musicmoz = property(fget=lambda x: x._props["musicmoz"].get(), fset=lambda x,y : x._props["musicmoz"].set(y), fdel=None, doc=propDocs["musicmoz"])
	opus = property(fget=lambda x: x._props["opus"].get(), fset=lambda x,y : x._props["opus"].set(y), fdel=None, doc=propDocs["opus"])
	performed_in = property(fget=lambda x: x._props["performed_in"].get(), fset=lambda x,y : x._props["performed_in"].set(y), fdel=None, doc=propDocs["performed_in"])
	tempo = property(fget=lambda x: x._props["tempo"].get(), fset=lambda x,y : x._props["tempo"].set(y), fdel=None, doc=propDocs["tempo"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___PublishedScore(mo___MusicalManifestation):
	"""
	mo:PublishedScore
	A published score (subclass of MusicalManifestation)
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicalManifestation.__init__(self)
		self._initialised = False
		self.shortname = "PublishedScore"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["publication_of"] = PropertySet("publication_of","http://purl.org/ontology/mo/publication_of", (mo___Signal,mo___Libretto,mo___Lyrics,mo___Score), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/PublishedScore"


	# Python class properties to wrap the PropertySet objects
	publication_of = property(fget=lambda x: x._props["publication_of"].get(), fset=lambda x,y : x._props["publication_of"].set(y), fdel=None, doc=propDocs["publication_of"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___SoloMusicArtist(foaf___Person, mo___MusicArtist):
	"""
	mo:SoloMusicArtist
	Single person whose musical creative work shows sensitivity and imagination.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicArtist.__init__(self)
		foaf___Person.__init__(self)
		self._initialised = False
		self.shortname = "SoloMusicArtist"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/SoloMusicArtist"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class frbr___Item(rdfs___Resource):
	"""
	frbr:Item
	"""
	def __init__(self,URI=None):
		# Initialise parents
		rdfs___Resource.__init__(self)
		self._initialised = False
		self.shortname = "Item"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["amazon_asin"] = PropertySet("amazon_asin","http://purl.org/ontology/mo/amazon_asin", foaf___Document, False)
		self._props["wikipedia"] = PropertySet("wikipedia","http://purl.org/ontology/mo/wikipedia", foaf___Document, False)
		self._initialised = True
	classURI = "http://purl.org/vocab/frbr/core#Item"


	# Python class properties to wrap the PropertySet objects
	amazon_asin = property(fget=lambda x: x._props["amazon_asin"].get(), fset=lambda x,y : x._props["amazon_asin"].set(y), fdel=None, doc=propDocs["amazon_asin"])
	wikipedia = property(fget=lambda x: x._props["wikipedia"].get(), fset=lambda x,y : x._props["wikipedia"].set(y), fdel=None, doc=propDocs["wikipedia"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class foaf___Group(foaf___Agent):
	"""
	foaf:Group
	A class of Agents.
	
		A group of agents.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Agent.__init__(self)
		self._initialised = False
		self.shortname = "Group"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["member"] = PropertySet("member","http://xmlns.com/foaf/0.1/member", foaf___Agent, False)
		self._initialised = True
	classURI = "http://xmlns.com/foaf/0.1/Group"


	# Python class properties to wrap the PropertySet objects
	member = property(fget=lambda x: x._props["member"].get(), fset=lambda x,y : x._props["member"].set(y), fdel=None, doc=propDocs["member"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___DiscreteTimeLine(timeline___TimeLine):
	"""
	timeline:DiscreteTimeLine
	A discrete time line (like the time line backing a digital signal
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___TimeLine.__init__(self)
		self._initialised = False
		self.shortname = "DiscreteTimeLine"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#DiscreteTimeLine"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class chord___ScaleInterval(chord___Interval):
	"""
	chord:ScaleInterval
	An interval in the root scale, made up of the degree of the scale and optional modifier.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		chord___Interval.__init__(self)
		self._initialised = False
		self.shortname = "ScaleInterval"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["degree"] = PropertySet("degree","http://purl.org/ontology/chord/degree", int, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/chord/ScaleInterval"


	# Python class properties to wrap the PropertySet objects
	degree = property(fget=lambda x: x._props["degree"].get(), fset=lambda x,y : x._props["degree"].set(y), fdel=None, doc=propDocs["degree"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___CorporateBody(foaf___Organization):
	"""
	mo:CorporateBody
	Organization or group of individuals and/or other organizations involved in the music market.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		foaf___Organization.__init__(self)
		self._initialised = False
		self.shortname = "CorporateBody"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["discogs"] = PropertySet("discogs","http://purl.org/ontology/mo/discogs", foaf___Document, False)
		self._props["download"] = PropertySet("download","http://purl.org/ontology/mo/download", foaf___Document, False)
		self._props["free_download"] = PropertySet("free_download","http://purl.org/ontology/mo/free_download", foaf___Document, False)
		self._props["imdb"] = PropertySet("imdb","http://purl.org/ontology/mo/imdb", foaf___Document, False)
		self._props["mailorder"] = PropertySet("mailorder","http://purl.org/ontology/mo/mailorder", foaf___Document, False)
		self._props["paid_download"] = PropertySet("paid_download","http://purl.org/ontology/mo/paid_download", foaf___Document, False)
		self._props["preview_download"] = PropertySet("preview_download","http://purl.org/ontology/mo/preview_download", foaf___Document, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/CorporateBody"


	# Python class properties to wrap the PropertySet objects
	discogs = property(fget=lambda x: x._props["discogs"].get(), fset=lambda x,y : x._props["discogs"].set(y), fdel=None, doc=propDocs["discogs"])
	download = property(fget=lambda x: x._props["download"].get(), fset=lambda x,y : x._props["download"].set(y), fdel=None, doc=propDocs["download"])
	free_download = property(fget=lambda x: x._props["free_download"].get(), fset=lambda x,y : x._props["free_download"].set(y), fdel=None, doc=propDocs["free_download"])
	imdb = property(fget=lambda x: x._props["imdb"].get(), fset=lambda x,y : x._props["imdb"].set(y), fdel=None, doc=propDocs["imdb"])
	mailorder = property(fget=lambda x: x._props["mailorder"].get(), fset=lambda x,y : x._props["mailorder"].set(y), fdel=None, doc=propDocs["mailorder"])
	paid_download = property(fget=lambda x: x._props["paid_download"].get(), fset=lambda x,y : x._props["paid_download"].set(y), fdel=None, doc=propDocs["paid_download"])
	preview_download = property(fget=lambda x: x._props["preview_download"].get(), fset=lambda x,y : x._props["preview_download"].set(y), fdel=None, doc=propDocs["preview_download"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Label(mo___CorporateBody):
	"""
	mo:Label
	Trade name of a company that produces musical works or expression of musical works.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___CorporateBody.__init__(self)
		self._initialised = False
		self.shortname = "Label"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Label"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Movement(mo___MusicalWork):
	"""
	mo:Movement
	A movement is a self-contained part of a musical work. While individual or selected movements from a composition are sometimes performed separately, a performance of the complete work requires all the movements to be performed in succession.

Often a composer attempts to interrelate the movements thematically, or sometimes in more subtle ways, in order that the individual
movements exert a cumulative effect. In some forms, composers sometimes link the movements, or ask for them to be played without a
pause between them.
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicalWork.__init__(self)
		self._initialised = False
		self.shortname = "Movement"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["movement_number"] = PropertySet("movement_number","http://purl.org/ontology/mo/movement_number", None, True)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Movement"


	# Python class properties to wrap the PropertySet objects
	movement_number = property(fget=lambda x: x._props["movement_number"].get(), fset=lambda x,y : x._props["movement_number"].set(y), fdel=None, doc=propDocs["movement_number"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___PublishedLibretto(mo___MusicalManifestation):
	"""
	mo:PublishedLibretto
	A published libretto
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicalManifestation.__init__(self)
		self._initialised = False
		self.shortname = "PublishedLibretto"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["publication_of"] = PropertySet("publication_of","http://purl.org/ontology/mo/publication_of", (mo___Signal,mo___Libretto,mo___Lyrics,mo___Score), False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/PublishedLibretto"


	# Python class properties to wrap the PropertySet objects
	publication_of = property(fget=lambda x: x._props["publication_of"].get(), fset=lambda x,y : x._props["publication_of"].set(y), fdel=None, doc=propDocs["publication_of"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___Torrent(mo___Medium):
	"""
	mo:Torrent
	Something available on the Bittorrent peer-2-peer filesharing network
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "Torrent"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/Torrent"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class timeline___ShiftMap(timeline___TimeLineMap):
	"""
	timeline:ShiftMap
	a map just shifting one timeline to another
	"""
	def __init__(self,URI=None):
		# Initialise parents
		timeline___TimeLineMap.__init__(self)
		self._initialised = False
		self.shortname = "ShiftMap"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["delay"] = PropertySet("delay","http://purl.org/NET/c4dm/timeline.owl#delay", None, False)
		self._initialised = True
	classURI = "http://purl.org/NET/c4dm/timeline.owl#ShiftMap"


	# Python class properties to wrap the PropertySet objects
	delay = property(fget=lambda x: x._props["delay"].get(), fset=lambda x,y : x._props["delay"].set(y), fdel=None, doc=propDocs["delay"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___DigitalSignal(mo___Signal):
	"""
	mo:DigitalSignal
	
		A digital signal
	
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Signal.__init__(self)
		self._initialised = False
		self.shortname = "DigitalSignal"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["bitsPerSample"] = PropertySet("bitsPerSample","http://purl.org/ontology/mo/bitsPerSample", None, True)
		self._props["sample_rate"] = PropertySet("sample_rate","http://purl.org/ontology/mo/sample_rate", None, True)
		self._props["sampled_version_of"] = PropertySet("sampled_version_of","http://purl.org/ontology/mo/sampled_version_of", mo___AnalogSignal, False)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/DigitalSignal"


	# Python class properties to wrap the PropertySet objects
	bitsPerSample = property(fget=lambda x: x._props["bitsPerSample"].get(), fset=lambda x,y : x._props["bitsPerSample"].set(y), fdel=None, doc=propDocs["bitsPerSample"])
	sample_rate = property(fget=lambda x: x._props["sample_rate"].get(), fset=lambda x,y : x._props["sample_rate"].set(y), fdel=None, doc=propDocs["sample_rate"])
	sampled_version_of = property(fget=lambda x: x._props["sampled_version_of"].get(), fset=lambda x,y : x._props["sampled_version_of"].set(y), fdel=None, doc=propDocs["sampled_version_of"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___MusicGroup(foaf___Group, mo___MusicArtist):
	"""
	mo:MusicGroup
	Group of musicians, or musical ensemble, usually popular or folk, playing parts of or improvising off of a musical arrangement. 
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___MusicArtist.__init__(self)
		foaf___Group.__init__(self)
		self._initialised = False
		self.shortname = "MusicGroup"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/MusicGroup"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class time___Instant(time___TemporalEntity):
	"""
	time:Instant
	 A time point (eg. "now":-) )
	"""
	def __init__(self,URI=None):
		# Initialise parents
		time___TemporalEntity.__init__(self)
		self._initialised = False
		self.shortname = "Instant"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["at"] = PropertySet("at","http://purl.org/NET/c4dm/timeline.owl#at", None, False)
		self._props["atDate"] = PropertySet("atDate","http://purl.org/NET/c4dm/timeline.owl#atDate", str, False)
		self._props["atDateTime"] = PropertySet("atDateTime","http://purl.org/NET/c4dm/timeline.owl#atDateTime", str, True)
		self._props["atDuration"] = PropertySet("atDuration","http://purl.org/NET/c4dm/timeline.owl#atDuration", str, True)
		self._props["atInt"] = PropertySet("atInt","http://purl.org/NET/c4dm/timeline.owl#atInt", int, False)
		self._props["atReal"] = PropertySet("atReal","http://purl.org/NET/c4dm/timeline.owl#atReal", float, False)
		self._props["atYear"] = PropertySet("atYear","http://purl.org/NET/c4dm/timeline.owl#atYear", int, False)
		self._props["atYearMonth"] = PropertySet("atYearMonth","http://purl.org/NET/c4dm/timeline.owl#atYearMonth", str, False)
		self._props["onTimeLine"] = PropertySet("onTimeLine","http://purl.org/NET/c4dm/timeline.owl#onTimeLine", timeline___TimeLine, False)
		self._props["inDateTime"] = PropertySet("inDateTime","http://www.w3.org/2006/time#inDateTime", time___DateTimeDescription, False)
		self._props["inXSDDateTime"] = PropertySet("inXSDDateTime","http://www.w3.org/2006/time#inXSDDateTime", str, False)
		self._initialised = True
	classURI = "http://www.w3.org/2006/time#Instant"


	# Python class properties to wrap the PropertySet objects
	at = property(fget=lambda x: x._props["at"].get(), fset=lambda x,y : x._props["at"].set(y), fdel=None, doc=propDocs["at"])
	atDate = property(fget=lambda x: x._props["atDate"].get(), fset=lambda x,y : x._props["atDate"].set(y), fdel=None, doc=propDocs["atDate"])
	atDateTime = property(fget=lambda x: x._props["atDateTime"].get(), fset=lambda x,y : x._props["atDateTime"].set(y), fdel=None, doc=propDocs["atDateTime"])
	atDuration = property(fget=lambda x: x._props["atDuration"].get(), fset=lambda x,y : x._props["atDuration"].set(y), fdel=None, doc=propDocs["atDuration"])
	atInt = property(fget=lambda x: x._props["atInt"].get(), fset=lambda x,y : x._props["atInt"].set(y), fdel=None, doc=propDocs["atInt"])
	atReal = property(fget=lambda x: x._props["atReal"].get(), fset=lambda x,y : x._props["atReal"].set(y), fdel=None, doc=propDocs["atReal"])
	atYear = property(fget=lambda x: x._props["atYear"].get(), fset=lambda x,y : x._props["atYear"].set(y), fdel=None, doc=propDocs["atYear"])
	atYearMonth = property(fget=lambda x: x._props["atYearMonth"].get(), fset=lambda x,y : x._props["atYearMonth"].set(y), fdel=None, doc=propDocs["atYearMonth"])
	onTimeLine = property(fget=lambda x: x._props["onTimeLine"].get(), fset=lambda x,y : x._props["onTimeLine"].set(y), fdel=None, doc=propDocs["onTimeLine"])
	inDateTime = property(fget=lambda x: x._props["inDateTime"].get(), fset=lambda x,y : x._props["inDateTime"].set(y), fdel=None, doc=propDocs["inDateTime"])
	inXSDDateTime = property(fget=lambda x: x._props["inXSDDateTime"].get(), fset=lambda x,y : x._props["inXSDDateTime"].set(y), fdel=None, doc=propDocs["inXSDDateTime"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___AudioFile(mo___Medium):
	"""
	mo:AudioFile
	An audio file, which may be available on a local file system or through http, ftp, etc.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "AudioFile"
		self.URI = URI
		self._props = getattr(self,"_props",{}) # Initialise if a parent class hasn't already
		self._props["encoding"] = PropertySet("encoding","http://purl.org/ontology/mo/encoding", None, True)
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/AudioFile"


	# Python class properties to wrap the PropertySet objects
	encoding = property(fget=lambda x: x._props["encoding"].get(), fset=lambda x,y : x._props["encoding"].set(y), fdel=None, doc=propDocs["encoding"])

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___SACD(mo___Medium):
	"""
	mo:SACD
	Super Audio Compact Disc used as medium to record a musical manifestation.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "SACD"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/SACD"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr

class mo___MD(mo___Medium):
	"""
	mo:MD
	Mini Disc used as medium to record a musical manifestation.
	"""
	def __init__(self,URI=None):
		# Initialise parents
		mo___Medium.__init__(self)
		self._initialised = False
		self.shortname = "MD"
		self.URI = URI
		self._initialised = True
	classURI = "http://purl.org/ontology/mo/MD"

	# Utility methods
	__setattr__ = protector
	__str__ = objToStr


# ======================= Instance Definitions ======================= 

timeline___universaltimeline = timeline___PhysicalTimeLine("http://purl.org/NET/c4dm/timeline.owl#universaltimeline")
timeline___universaltimeline.description = \
"""The timeline one can addresss "the 1st of July, 2007"
The "canonical" physical time-line, on which points/intervals are addressed through UTC.
		(Remember: we do here the amalgam between timelines and coordinate systems, as we 
		choose one canonical one per timeline)."""

chord___aug = chord___Chord("http://purl.org/ontology/chord/aug")
chord___dim = chord___Chord("http://purl.org/ontology/chord/dim")
chord___dim7 = chord___Chord("http://purl.org/ontology/chord/dim7")
chord___hdim7 = chord___Chord("http://purl.org/ontology/chord/hdim7")
chord___maj = chord___Chord("http://purl.org/ontology/chord/maj")
chord___maj6 = chord___Chord("http://purl.org/ontology/chord/maj6")
chord___maj7 = chord___Chord("http://purl.org/ontology/chord/maj7")
chord___maj9 = chord___Chord("http://purl.org/ontology/chord/maj9")
chord___min = chord___Chord("http://purl.org/ontology/chord/min")
chord___min6 = chord___Chord("http://purl.org/ontology/chord/min6")
chord___min7 = chord___Chord("http://purl.org/ontology/chord/min7")
chord___min9 = chord___Chord("http://purl.org/ontology/chord/min9")
chord___minmaj7 = chord___Chord("http://purl.org/ontology/chord/minmaj7")
chord___ninth = chord___Chord("http://purl.org/ontology/chord/ninth")
chord___noChord = chord___Chord("http://purl.org/ontology/chord/noChord")
chord___seventh = chord___Chord("http://purl.org/ontology/chord/seventh")
chord___sus4 = chord___Chord("http://purl.org/ontology/chord/sus4")

chord___doubleflat = chord___Modifier("http://purl.org/ontology/chord/doubleflat")
chord___doublesharp = chord___Modifier("http://purl.org/ontology/chord/doublesharp")
chord___flat = chord___Modifier("http://purl.org/ontology/chord/flat")
chord___sharp = chord___Modifier("http://purl.org/ontology/chord/sharp")

note___A = chord___Natural("http://purl.org/ontology/chord/note/A")
note___B = chord___Natural("http://purl.org/ontology/chord/note/B")
note___C = chord___Natural("http://purl.org/ontology/chord/note/C")
note___D = chord___Natural("http://purl.org/ontology/chord/note/D")
note___E = chord___Natural("http://purl.org/ontology/chord/note/E")
note___F = chord___Natural("http://purl.org/ontology/chord/note/F")
note___G = chord___Natural("http://purl.org/ontology/chord/note/G")

note___Ab = chord___Note("http://purl.org/ontology/chord/note/Ab")
note___As = chord___Note("http://purl.org/ontology/chord/note/As")
note___Bb = chord___Note("http://purl.org/ontology/chord/note/Bb")
note___Bs = chord___Note("http://purl.org/ontology/chord/note/Bs")
note___Cb = chord___Note("http://purl.org/ontology/chord/note/Cb")
note___Cs = chord___Note("http://purl.org/ontology/chord/note/Cs")
note___Db = chord___Note("http://purl.org/ontology/chord/note/Db")
note___Ds = chord___Note("http://purl.org/ontology/chord/note/Ds")
note___Eb = chord___Note("http://purl.org/ontology/chord/note/Eb")
note___Es = chord___Note("http://purl.org/ontology/chord/note/Es")
note___Fb = chord___Note("http://purl.org/ontology/chord/note/Fb")
note___Fs = chord___Note("http://purl.org/ontology/chord/note/Fs")
note___Gb = chord___Note("http://purl.org/ontology/chord/note/Gb")
note___Gs = chord___Note("http://purl.org/ontology/chord/note/Gs")

mo___bootleg = mo___ReleaseStatus("http://purl.org/ontology/mo/bootleg")
mo___bootleg.description = \
"""An unofficial/underground musical work or the expression of a musical work that was not sanctioned by the artist and/or the corporate body."""
mo___official = mo___ReleaseStatus("http://purl.org/ontology/mo/official")
mo___official.description = \
"""Any musical work or the expression of a musical work officially sanctioned by the artist and/or their corporate body."""
mo___promotion = mo___ReleaseStatus("http://purl.org/ontology/mo/promotion")
mo___promotion.description = \
"""A giveaway musical work or the expression of a musical work intended to promote an upcoming official musical work or the expression of a musical work."""

mo___album = mo___ReleaseType("http://purl.org/ontology/mo/album")
mo___album.description = \
"""One or more track issued together.
    		This is a type of MusicalManifestation defined by the musical industry."""
mo___audiobook = mo___ReleaseType("http://purl.org/ontology/mo/audiobook")
mo___audiobook.description = \
"""Book read by a narrator without music.
		This is a type of MusicalManifestation defined by the musical industry."""
mo___compilation = mo___ReleaseType("http://purl.org/ontology/mo/compilation")
mo___compilation.description = \
"""Collection of previously released manifestations of a musical expression by one or more artists.
		This is a type of MusicalManifestation defined by the musical industry."""
mo___ep = mo___ReleaseType("http://purl.org/ontology/mo/ep")
mo___ep.description = \
"""An EP"""
mo___interview = mo___ReleaseType("http://purl.org/ontology/mo/interview")
mo___interview.description = \
"""Recording of the questioning of a person.
		This is a type of MusicalManifestation defined by the musical industry."""
mo___live = mo___ReleaseType("http://purl.org/ontology/mo/live")
mo___live.description = \
"""A musical manifestation that was recorded live.
		This is a type of MusicalManifestation defined by the musical industry."""
mo___remix = mo___ReleaseType("http://purl.org/ontology/mo/remix")
mo___remix.description = \
"""Musical manifestation that primarily contains remixed material. 
		This is a type of MusicalManifestation defined by the musical industry."""
mo___soundtrack = mo___ReleaseType("http://purl.org/ontology/mo/soundtrack")
mo___soundtrack.description = \
"""Sound recording on a narrow strip of a motion picture film.
		This is a type of MusicalManifestation defined by the musical industry."""
mo___spokenword = mo___ReleaseType("http://purl.org/ontology/mo/spokenword")
mo___spokenword.description = \
"""Spoken word is a form of music or artistic performance in which lyrics, poetry, or stories are spoken rather than sung. 
		Spoken-word is often done with a musical background, but emphasis is kept on the speaker.
		This is a type of MusicalManifestation defined by the musical industry."""

time___Friday = time___DayOfWeek("http://www.w3.org/2006/time#Friday")
time___Monday = time___DayOfWeek("http://www.w3.org/2006/time#Monday")
time___Saturday = time___DayOfWeek("http://www.w3.org/2006/time#Saturday")
time___Sunday = time___DayOfWeek("http://www.w3.org/2006/time#Sunday")
time___Thursday = time___DayOfWeek("http://www.w3.org/2006/time#Thursday")
time___Tuesday = time___DayOfWeek("http://www.w3.org/2006/time#Tuesday")
time___Wednesday = time___DayOfWeek("http://www.w3.org/2006/time#Wednesday")

time___unitDay = time___TemporalUnit("http://www.w3.org/2006/time#unitDay")
time___unitHour = time___TemporalUnit("http://www.w3.org/2006/time#unitHour")
time___unitMinute = time___TemporalUnit("http://www.w3.org/2006/time#unitMinute")
time___unitMonth = time___TemporalUnit("http://www.w3.org/2006/time#unitMonth")
time___unitSecond = time___TemporalUnit("http://www.w3.org/2006/time#unitSecond")
time___unitWeek = time___TemporalUnit("http://www.w3.org/2006/time#unitWeek")
time___unitYear = time___TemporalUnit("http://www.w3.org/2006/time#unitYear")

namespaceBindings = {"":"http://www.w3.org/2002/07/owl#","owl":"http://www.w3.org/2002/07/owl#","chord":"http://purl.org/ontology/chord/","frbr":"http://purl.org/vocab/frbr/core#","vs":"http://www.w3.org/2003/06/sw-vocab-status/ns#","event":"http://purl.org/NET/c4dm/event.owl#","xml":"http://www.w3.org/XML/1998/namespace","rdfs":"http://www.w3.org/2000/01/rdf-schema#","wot":"http://xmlns.com/wot/0.1/","note":"http://purl.org/ontology/chord/note/","default1":"http://www.w3.org/2006/time#","daml":"http://www.daml.org/2001/03/daml+oil#","default2":"http://purl.org/NET/c4dm/timeline.owl#","dcterms":"http://purl.org/dc/terms/","foaf":"http://xmlns.com/foaf/0.1/","bio":"http://vocab.org/bio/0.1/","timeline":"http://purl.org/NET/c4dm/timeline.owl#","dc":"http://purl.org/dc/elements/1.1/","key":"http://purl.org/NET/c4dm/keys.owl#","tzont":"http://www.w3.org/2006/timezone#","geo":"http://www.w3.org/2003/01/geo/wgs84_pos#","mo":"http://purl.org/ontology/mo/","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","xsd":"http://www.w3.org/2001/XMLSchema#","time":"http://www.w3.org/2006/time#"}



# =======================       Clean Up       ======================= 
del objToStr, propDocs
