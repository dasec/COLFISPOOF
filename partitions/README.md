# COLFISPOOF partition files

## Ground truth
Contains 100 samples each for 72 different PAI species. A summary of all 72 PAI species is given in the table below.

| **PAI**              | **material**   | **LOO group** | | **PAI**                        | **material**   | **LOO group**    |
|----------------------|----------------|---------------|-|--------------------------------|----------------|------------------|
| wood glue            | glue           | default color | | printout blue                  | paper printout | printout         |
| knetosil 45          | knetosil       | default color | | printout blue light            | paper printout | printout         |
| knetosil 90          | knetosil       | default color | | printout green                 | paper printout | printout         |
| latex fashion flesh  | latex          | default color | | printout green light           | paper printout | printout         |
| modelling clay       | modelling clay | default color | | printout orange                | paper printout | printout         |
| moldable glue blue   | moldable glue  | default color | | printout orange light          | paper printout | printout         |
| moldable glue brown  | moldable glue  | default color | | printout red                   | paper printout | printout         |
| moldable glue green  | moldable glue  | default color | | printout rose                  | paper printout | printout         |
| moldable glue grey   | moldable glue  | default color | | printout white                 | paper printout | printout         |
| moldable glue orange | moldable glue  | default color | | printout yellow                | paper printout | printout         |
| moldable glue pink   | moldable glue  | default color | | printout yellow light          | paper printout | printout         |
| moldable glue red    | moldable glue  | default color | | printout syncolfinger          | paper printout | printout         |
| moldable glue white  | moldable glue  | default color | |                                |                |                  |
| moldable glue yellow | moldable glue  | default color | | ds original                    | dragonskin     | transparent      |
| playdoh blue         | playdoh        | default color | | ds brown transparent           | dragonskin     | transparent      |
| playdoh blue light   | playdoh        | default color | | gelafix                        | gelafix        | transparent      |
| playdoh brown dark   | playdoh        | default color | | gelatin fx                     | gelatin        | transparent      |
| playdoh brown light  | playdoh        | default color | | school glue                    | glue           | transparent      |
| playdoh green dark   | playdoh        | default color | |                                |                |                  |
| playdoh green light  | playdoh        | default color | | ds brown                       | dragonskin     | colored silicone |
| playdoh orange       | playdoh        | default color | | ds brown darkred               | dragonskin     | colored silicone |
| playdoh orange neon  | playdoh        | default color | | ds darkred                     | dragonskin     | colored silicone |
| playdoh pink         | playdoh        | default color | | ds darkred brown               | dragonskin     | colored silicone |
| playdoh pink pale    | playdoh        | default color | | ds darkred brown yellow        | dragonskin     | colored silicone |
| playdoh purple       | playdoh        | default color | | ds orange                      | dragonskin     | colored silicone |
| playdoh purple dark  | playdoh        | default color | | ds orange brown                | dragonskin     | colored silicone |
| playdoh red          | playdoh        | default color | | ds orange brown dark           | dragonskin     | colored silicone |
| playdoh teal         | playdoh        | default color | | ds orange brown darkred        | dragonskin     | colored silicone |
| playdoh white        | playdoh        | default color | | ds orange brown light          | dragonskin     | colored silicone |
| playdoh yellow       | playdoh        | default color | | ds orange dirty                | dragonskin     | colored silicone |
| playdoh yellow light | playdoh        | default color | | ds red                         | dragonskin     | colored silicone |
| sillyputty gold      | silly putty    | default color | | ds red brown                   | dragonskin     | colored silicone |
| sillyputty green     | silly putty    | default color | | ds yellow                      | dragonskin     | colored silicone |
| sillyputty pink      | silly putty    | default color | | ds yellow brown                | dragonskin     | colored silicone |
| sillyputty red       | silly putty    | default color | | ef brown yellow darkred        | ecoflex        | colored silicone |
| sillyputty silver    | silly putty    | default color | | ef brown yellow darkred orange | ecoflex        | colored silicone |
| sillyputty yellow    | silly putty    | default color | | ef yellow brown dirty          | ecoflex        | colored silicone |

## Baseline
Splits all samples into *train*, *valid*, and *test* partitions to be used to train contactless fingerprint PAD methods. Samples are randomly assigned to the partitions based on the shares: 30% train, 20% valid, and 50% test. Each PAI species is available for training, validation, and testing.

## LOO protocols
The leave one out (LOO) protocols group all PAI species according to their visual properties into four defined groups:
* printout
* transparent
* default color
* colored silicone

The goal is to evaluate the generalization capabilities of the PAD methods towards unknown attacks. Hence, a full group of PAI species is neither included in training nor validation sets and only seen during testing. The remaining, or known, PAI species are split into 70% training and 30% validation partitions.


