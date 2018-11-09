#include <iostream>
#include <glbinding/gl/gl.h>
#include <glbinding-aux/RingBuffer.h>
using namespace gl;

int main()
{
	glbinding::aux::RingBuffer<int> buffer(10);

    return 0;
}