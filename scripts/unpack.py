from ofrak import *
from ofrak.core import *


async def main(ofrak_context: OFRAKContext, root_resource: Optional[Resource] = None):
    await root_resource.unpack()


if __name__ == "__main__":
    ofrak = OFRAK()
    if False:
        import ofrak_angr
        import ofrak_capstone

        ofrak.discover(ofrak_capstone)
        ofrak.discover(ofrak_angr)

    if False:
        import ofrak_binary_ninja
        import ofrak_capstone

        ofrak.discover(ofrak_capstone)
        ofrak.discover(ofrak_binary_ninja)

    if False:
        import ofrak_ghidra

        ofrak.discover(ofrak_ghidra)

    ofrak.run(main)
