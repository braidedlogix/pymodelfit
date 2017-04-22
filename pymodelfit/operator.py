import collections.abc as abc

def isMappingType(obj):
    return isinstance(obj, abc.Mapping)
def isSequenceType(obj):
    return isinstance(obj, abc.Sequence)