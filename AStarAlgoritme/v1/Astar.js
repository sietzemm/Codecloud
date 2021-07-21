// Date 22-02-2019
function removeFromArray(arr, elt){
    for( var i = arr.length - 1; i >= 0; i--){
        if(arr[i] == elt){
            arr.splice(i, 1);
        }
    }
}

function heuristic(a,b){
    var d = dist(a.i, a.j, b.i, b.j);
    return d;
}

var cols = 50;
var rows = 50;
var grid = new Array(cols);

var open_set = [];
var closed_set = [];

var start;
var end;
var w,h;

function Spot(i, j){
    this.i = i;
    this.j = j;  
	this.f = 0;
    this.g = 0;
    this.h = 0;
    this.neighbors = [];
    this.previous = undefined;

    this.show = function(col){
        fill(col);
        noStroke();
        rect(this.i * w, this.j * h, w - 1,h - 1);
        }

        this.addNeighbors = function(grid){
        var i = this.i;
        var j = this.j;
        
        // all neighbors        
        if(i < cols-1) {
            this.neighbors.push(grid[i + 1][j]);
        }
        if ( i > 0) {
            this.neighbors.push(grid[i - 1] [j]);
        }
        if( j < rows - 1) {
            this.neighbors.push(grid[i][j + 1]);
        }
        if(j > 0){
            this.neighbors.push(grid[i][j - 1]);

        }
    }

}

function setup() {
    createCanvas(400,400);
    console.log('A*');

    w = width / cols;
    h = height / rows;

    // make a 2d Array
    for(var i =0; i < cols; i++){
        grid[i] = new Array(rows); 
    }

    for(var i = 0; i < cols; i++){
        for(var j = 0; j < rows; j++){
            grid[i][j] = new Spot(i,j);
        }
    }

    
    for(var i = 0; i < cols; i++){
        for(var j = 0; j < rows; j++){
            grid[i][j].addNeighbors(grid);
        }
    }

    start = grid[0][0];
    end = grid[cols - 1][rows - 1];

    open_set.push(start);

}

function draw(){
    if(open_set.length > 0){
        // keep going
        var winner = 0;
        for(var i = 0; i < open_set.length; i++){
            if(open_set[i].f < open_set[winner].f){
                winner = i;
            }
        }
        var current = open_set[winner];

        if(open_set[winner] === end){
            console.log("end");
        }

        removeFromArray(open_set, current);
        closed_set.push(current);

        var neighbors = current.neighbors;
        for(var i = 0; i < neighbors.length; i++){
            var neighbor = neighbors[i];

            if(!closed_set.includes(neighbor)){
                var tempG = current.g + 1;

                if(open_set.includes(neighbor)){
                    if(tempG < neighbor.g){
                        neighbor.g = tempG;
                    }
                } else {
                    neighbor.g = tempG;
                    open_set.push(neighbor);
                }

                neighbor.h = heuristic(neighbor, end);
                neighbor.f = neighbor.g + neighbor.h;
                neighbor.previous = current;
            }
            neighbor.g = current.g + 1;
        }

    } else {
        // no solution
    }
    background(0);

    for(var i = 0; i < cols; i++){
        for( var j = 0; j < rows; j++){
            grid[i][j].show(color(255));
        }
    }

    for (var i = 0; i < closed_set.length; i++){
        closed_set[i].show(color(255,0,0));
    }

    for (var i = 0; i < open_set.length; i++){
        open_set[i].show(color(0,222,0));
    }
}