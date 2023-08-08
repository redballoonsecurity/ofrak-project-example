from ofrak import *
from ofrak.core import *


async def main(ofrak_context: OFRAKContext, root_resource: Optional[Resource] = None):
    await root_resource.unpack_recursively()

    coderegion_0x400530 = await root_resource.get_only_child(
        r_filter=ResourceFilter(
            tags={CodeRegion, ElfSection},
            attribute_filters=[
                ResourceAttributeValueFilter(
                    attribute=AttributesType[Addressable].VirtualAddress, value=4195632
                )
            ],
        )
    )

    await coderegion_0x400530.run(
        AddCommentModifier,
        AddCommentModifierConfig(
            (Range(0x0, 0x1A2), "We have made modification to the code here")
        ),
    )

    await root_resource.run(
        AddCommentModifier,
        AddCommentModifierConfig(
            (Range(0x0, 0x2070), "Follow the comments to see what we changed")
        ),
    )

    linkablesymbol_0x40063a = await coderegion_0x400530.get_only_child(
        r_filter=ResourceFilter(
            tags={LinkableSymbol, ComplexBlock},
            attribute_filters=[
                ResourceAttributeValueFilter(
                    attribute=AttributesType[Addressable].VirtualAddress, value=4195898
                )
            ],
        )
    )

    await linkablesymbol_0x40063a.run(
        AddCommentModifier,
        AddCommentModifierConfig((Range(0x0, 0x26), "Modifications to main here. ")),
    )

    basicblock_0x40063a = await linkablesymbol_0x40063a.get_only_child(
        r_filter=ResourceFilter(
            tags={BasicBlock},
            attribute_filters=[
                ResourceAttributeValueFilter(
                    attribute=AttributesType[Addressable].VirtualAddress, value=4195898
                )
            ],
        )
    )

    await basicblock_0x40063a.run(
        AddCommentModifier,
        AddCommentModifierConfig((Range(0x0, 0x10), "We changed this basic block ")),
    )

    instruction_0x400645 = await basicblock_0x40063a.get_only_child(
        r_filter=ResourceFilter(
            tags={Instruction},
            attribute_filters=[
                ResourceAttributeValueFilter(
                    attribute=AttributesType[Addressable].VirtualAddress, value=4195909
                )
            ],
        )
    )

    instruction_0x400645.queue_patch(Range(0x0, 0x5), b"\xe8\x19\xff\xff\xff")

    await instruction_0x400645.save()
    await instruction_0x400645.auto_run(all_analyzers=True)
    await basicblock_0x400645.run(
        AddCommentModifier,
        AddCommentModifierConfig((Range(0x0, 0x5), "We modified this instruction to perform an infinite loop instead of calling printf")),
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
