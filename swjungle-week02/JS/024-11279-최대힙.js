//  45	43313391	15	marshal1101	23992KB	260ms	node.js 	2109B	

const input = require('fs').readFileSync(
    'test.txt'
).toString().trim().split('\n').map(Number);

class MaxHeap {
    constructor() {
        this.heap = [ null ];
    }
    
    size() {
        return this.heap.length - 1;
    }
    
    getMax() {
        return this.heap[1] ? this.heap[1] : null;
    }
    
    swap(a, b) {
        [ this.heap[a], this.heap[b] ] = [ this.heap[b], this.heap[a] ];
    }
    
    heappush(value) {
        this.heap.push(value);
        let curIdx = this.heap.length - 1;
        let parIdx = (curIdx / 2) >> 0;
        
        while(curIdx > 1 && this.heap[parIdx] < this.heap[curIdx]) {
            this.swap(parIdx, curIdx)
            curIdx = parIdx;
            parIdx = (curIdx / 2) >> 0;
        }
    }
    
    heappop() {
        const max = this.heap[1];	
        if(this.heap.length <= 2) this.heap = [ null ];
        else this.heap[1] = this.heap.pop();   
        
        let curIdx = 1;
        let leftIdx = curIdx * 2;
        let rightIdx = curIdx * 2 + 1; 
        
        if(!this.heap[leftIdx]) return max;
        if(!this.heap[rightIdx]) {
            if(this.heap[leftIdx] > this.heap[curIdx]) {
                this.swap(leftIdx, curIdx);
            }
            return max;
        }

        while(this.heap[leftIdx] > this.heap[curIdx] || this.heap[rightIdx] > this.heap[curIdx]) {
            const maxIdx = this.heap[leftIdx] < this.heap[rightIdx] ? rightIdx : leftIdx;
            this.swap(maxIdx, curIdx);
            curIdx = maxIdx;
            leftIdx = curIdx * 2;
            rightIdx = curIdx * 2 + 1;
        }

        return max;
    }
}

function solution(input) {
    let result = '';
    const heapArr = new MaxHeap;
    const N = +input[0];

    // 시작
    for (let i = 1; i <= N; i++) {
        if (input[i] === 0) {
            if (heapArr.size() > 0) {
                result += heapArr.heappop() + "\n";
            } else {
                result += "0\n";
            }
        }
        else {
            heapArr.heappush(input[i]);
        }
    }

    return result;
}

console.log(solution(input));