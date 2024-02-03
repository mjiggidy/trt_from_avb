import enum, avb

class MobTypes(enum.IntEnum):
	"""Mob Types"""

	# NOTE: Data originates from `avb.trackgrouns.Compositon.mob_type` property
	
	COMPOSITION_MOB   = 1
	"""Composition Mob"""
	MASTER_MOB        = 2
	"""Master Clip"""
	SOURCE_MOB        = 3
	"""Tape, Source File, or Film Reel"""

	@classmethod
	def from_composition(cls, comp:avb.trackgroups.Composition):
		return cls(comp.mob_type_id)
	

class MobUsage(enum.IntEnum):
	"""Mob Usage"""
	
	# NOTE: From pyavb: `these usage codes seem to come from omf`
	# TODO: Marry these to `.bins.BinDisplayOptions`?

	UNDEFINED    = 0 # TODO: Investigate - Top level...?
	PRECOMPUTE   = 1
	SUBCLIP      = 2
	EFFECT       = 3
	GROUP_CLIP   = 4
	GROUP_OOFTER = 5 # wat is oofter plz advise
	MOTION       = 6
	MASTER_MOB   = 7
	PRECOMPUTE_FILE  = 9
	PRECOMPUTE_SOURCE_MOB = 14 # Need clarification

	@classmethod
	def from_composition(cls, comp:avb.trackgroups.Composition):
		return cls(comp.usage_code)

def composition_is_toplevel(comp:avb.trackgroups.Composition) -> bool:
	"""Determine if a given composition is a top-level timeline"""
	# NOTE: Using rules from `avb.bin.Bin.toplevel()``
	return MobTypes.from_composition(comp) == MobTypes.COMPOSITION_MOB and MobUsage.from_composition(comp) == MobUsage.UNDEFINED