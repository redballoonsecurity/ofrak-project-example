from ofrak import *
from ofrak.core import *


async def main(ofrak_context: OFRAKContext, root_resource: Optional[Resource] = None):
    await root_resource.unpack_recursively()

    elfprogramheader_0xb0 = await root_resource.get_only_child(
        r_filter=ResourceFilter(
            tags={ElfProgramHeader},
            attribute_filters=[
                ResourceAttributeValueFilter(attribute=Data.Offset, value=176)
            ],
        )
    )

    await elfprogramheader_0xb0.run(
        AddCommentModifier,
        AddCommentModifierConfig((Range(0x0, 0x38), "Segment 2 is Read/Executable")),
    )

    elfprogramheader_0xe8 = await root_resource.get_only_child(
        r_filter=ResourceFilter(
            tags={ElfProgramHeader},
            attribute_filters=[
                ResourceAttributeValueFilter(attribute=Data.Offset, value=232)
            ],
        )
    )

    await elfprogramheader_0xe8.run(
        AddCommentModifier,
        AddCommentModifierConfig((Range(0x0, 0x38), "Segment 3 is Read/Write")),
    )

    elfsection_0x530 = await root_resource.get_only_child(
        r_filter=ResourceFilter(
            tags={ElfSection, CodeRegion},
            attribute_filters=[
                ResourceAttributeValueFilter(attribute=Data.Offset, value=1328)
            ],
        )
    )

    await elfsection_0x530.run(
        AddCommentModifier,
        AddCommentModifierConfig(
            (Range(0x0, 0x1A2), "This section contains the program's code")
        ),
    )


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
