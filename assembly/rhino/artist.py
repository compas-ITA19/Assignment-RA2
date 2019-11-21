class AssemblyArtist(object):
    """Rudimentary assembly artist for RhinoPython
    """

    def __init__(self, assembly):
        self.assembly = assembly

    def draw(self):
        from compas_rhino.artists import MeshArtist
        for vkey, element in self.assembly.elements():
            artist = MeshArtist(element.mesh)
            artist.draw_mesh()