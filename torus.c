#include <math.h>
#include <stdio.h>

#define pi 3.1415

float A, B, C;
const int screenWidth = 160, screenHeight = 44;
const float phi_step = 0.05;      // this is the angle of rotation on y axis
const float theta_step = 0.07;    // this is the angle of rotation in the cross section of the torus

const float R1 = 5, R2 = 10;        // R1 is the radius of the torus with respect to the y axis
                            // R2 is the radius of the cross setion of the torus

const float K2 = 50; // distance from observer to torus

const float K1 = screenWidth*K2*3/(8*(R1+R2)); // distance from observer to screen

// const float K1 = screen_width*K2*3/(8*(R1+R2));
int light[] = {0, -1 , 1};

// char light_map[] = {'.', ',', '*', ';', '/', '%', '@'};
char light_map[] = {'.', ',', '-', '~', ':', ';', '=', '!', '*', '#', '$', '@'};

// declare screen buffers output
char output[160 * 44];
float zbuffer[160 * 44];

char* torusTick() {
    // printf("whatsapp");
    for (int i = 0; i < screenHeight; i++) {
        for (int j = 0; j < screenWidth; j++) {
            output[i*screenWidth + j] = ' ';
            zbuffer[i*screenWidth + j] = 0;
        }
    }
    // printf("whatsapp2");
    for (float phi = 0; phi < 2*pi; phi+=phi_step) {
        for (float theta = 0; theta < 2*pi; theta+=theta_step) {
            float cosTheta = cos(theta);
            float sinTheta = sin(theta);
            float cosPhi = cos(phi);
            float sinPhi = sin(phi);
            float cosA = cos(A);
            float sinA = sin(A);
            float cosB = cos(B);
            float sinB = sin(B);
            float sinC = sin(C);
            float cosC = cos(C);
            
            float circlex = R2 + R1*cosTheta;
            float circley = R1*sinTheta;

            float x = circlex * (cosB * cosPhi + sinA * sinPhi) - circley * cosA * sinB;
            float y = circlex * (sinB * cosPhi - sinA * cosB * sinPhi) + circley * cosA * cosB;
            float z = K2 + cosA * circlex * sinPhi + circley * sinA;

            // rotate
            // float xr = -z*sinB + cosB*(x*cosA + y*sinA); 
            // float yr = y*cosA - x*sinA;
            // float zr = z*cosB + sinB*(x*cosA + y*sinA);
            
            // float xr = -z*sinB + cosB * (x*cosA + y*sinA);
            // float yr = cosC * (y*cosA - x*sinA) + sinC*(z*cosB + sinB*(x*cosA + y*sinA));
            // float zr = cosC * (z*cosB + sinB * (x*cosA + y*sinA)) - sinC*(y*cosA - x*sinA);
            
            // float x = cosB*cosPhi*circlex - circley*sinB;
            // float y = circley*cosA*cosB + circlex*(cosA*sinB*cosPhi + sinA*sinPhi);
            // float z = circley*sinA*cosB + circlex*(sinA*sinB*cosPhi - cosA*sinPhi) + K2;
            // printf("(x=%f, y=%f, z=%f\n)", x, y, z);
            // printf("(theta=%f, phi=%f, R1=%f, R2=%f)", theta, phi, R1, R2);

            // char ab[2];
            // fgets(ab, 2, stdin);

            // project to screen
            int xp = (int)(screenWidth/2 + x * K2 / z);
            int yp = (int)(screenHeight/2 - y * K2 / z); // y is inverted
            // printf("whatsapp5");
            // printf("%f\n", 1/zr);
            // printf("phi: %f, theta: %f, x: %f, y: %f, z: %f, xp: %d, yp: %d\n", phi, theta, x, y, z, xp, yp);
            if (xp >= 0 && xp < screenWidth && yp >= 0 && yp < screenHeight) {
                int index = yp*screenWidth + xp;
                // printf("index: %d\n", index);
            
                if (index<screenHeight*screenWidth && zbuffer[index] < 1/z) {
                    zbuffer[index] = 1/z;
                    // dot product to map the lighting  
                    // float mx = light[0] * cosB*cosPhi*cosTheta - sinB*sinTheta;
                    // float my = light[1] * cosTheta*(cosA*sinB*cosPhi + sinA*sinPhi) + cosA*cosB*sinTheta;
                    // float mz = light[2] * cosTheta*(sinA*sinB*cosPhi - cosA*sinPhi) + sinA*cosB*sinTheta;
                    // float magnitude = mx + my + mz;

                    float magnitude = cosPhi*cosTheta*sinB - cosA*cosTheta*sinPhi - sinA*sinTheta + cosB*(cosA*sinTheta - cosTheta*sinA*sinPhi);
                    // printf("magnitude: %f\n", magnitude);
                    // float magnitude = cosPhi*cosTheta*sinB - cosA*cosTheta*sinPhi - sinA*sinPhi + cosB*(cosA*sinTheta - cosTheta*sinA*sinPhi);
                    int light_map_size = sizeof(light_map);
                    int magnitude_idx;
                    if (magnitude<0){
                        magnitude_idx = 0; 
                    } else {
                        magnitude_idx = (int) (magnitude * 8);
                    }
                    
                    output[index] = light_map[magnitude_idx];
                    // printf("whatsapp6");  
                } 
            }
        }
    }
    return output;
}

int main() {
    A = 0;
    B = 0;
    C = 0;
    while (1) {
        // printf("hey");
        char* output = torusTick();
        printf("\x1b[H");
        for (int i = 0; i < screenHeight; i++) {
            for (int j = 0; j < screenWidth; j++) {
                putchar(output[i*screenWidth + j]);
            }
            putchar('\n');
        }
        // char ab[2];
        // fgets(ab, 2, stdin);
        A += 0.002;
        B += 0.001;
        // C += 0.01;
    }
    return 0;
}

