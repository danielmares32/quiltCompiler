# quiltCompiler
Little Quilt Compiler Implementation in PLY

Little Quilt is a small language introduced by Ravi Sethi in his book ‘Programming Languages’. Here, a restricted version of Little Quilt is presented.

The language is defined by the following BNF grammar:

\<QUILT> ::= A | B | turn(\<QUILT>) | sew(\<QUILT>,\<QUILT>)

A and B represent the two primitive quilts. Each primitive quilt corresponds to a matricial arrangement of 2 × 2 characters. turn() and sew() are operations over quilts.

The instruction turn(x) turns the quilt x 90 degrees clockwise. The following table illustrates the primitive quilts as well as examples of the effect of the turn() operation:

![image](https://user-images.githubusercontent.com/53630621/194089895-969a9db3-4720-491d-99a0-79cf9362555f.png)

Accordingly, the instruction sew(x,y) sews quilt x to the left of quilt y. Both x and y must have the same height, otherwise an error will be generated. The following figure represents the result of sew(A,turn(B)):

![image](https://user-images.githubusercontent.com/53630621/194090343-558d7127-29df-46d6-947b-4d03c50e1683.png)

while the sew(turn(sew(B,turn(B))),A) generates an error message.
