#include<stdio.h>
#include<math.h>

int main(){

float bcast[78]={121 ,
277 ,
537 ,
198 ,
117 ,
361 ,
481 ,
518 ,
313 ,
671 ,
274 ,
492 ,
502 ,
107 ,
257 ,
346 ,
478 ,
114 ,
302 ,
536 ,
426 ,
516 ,
209 ,
206 ,
471 ,
297 ,
169 ,
358 ,
453 ,
176 ,
452 ,
285 ,
81 ,
442 ,
517 ,
138 ,
448 ,
445 ,
298 ,
413 ,
127 ,
387 ,
634 ,
109 ,
618 ,
153 ,
493 ,
452 ,
445 ,
258 ,
234 ,
302 ,
515 ,
385 ,
307 ,
39 ,
120 ,
79 ,
487 ,
190 ,
416 ,
600 ,
312 ,
316 ,
248 ,
428 ,
371 ,
36 ,
398 ,
527 ,
448 ,
589 ,
400 ,
480 ,
446 ,
512 ,
80 ,
97 };
int count = 0;
float sum = 0;
for (int i=0;i<78;i++){
	if(bcast[i] != 0){
	sum += bcast[i];
	count++;
	}
}
printf("count=%d\n",count);

float mean=sum/count;
printf("mean=%f\n",mean);
float diff[78]={0};
for(int i=0;i<count;i++){
	diff[i] = pow((bcast[i]-mean),2);
}
sum =0;
for(int i=0;i<count;i++){
	sum += diff[i];
}
float sd =  sqrt(sum/count);
printf("99CI =%f\n",3.291*(sd/sqrt(count)));
printf("99CI upper=%f\n",mean + 3.291*(sd/sqrt(count)));
printf("99CI lower=%f\n",mean - 3.291*(sd/sqrt(count)));
return 0;
}
