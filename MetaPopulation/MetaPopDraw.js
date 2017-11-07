var MetaPopulationVisualization = function(space_width, space_height, canvas_width, canvas_height, context){

    var currentFrame = 0

    var drawEvery = 1

    // console.log(space_width)
    // console.log(space_height)
    // console.log(canvas_width)
    // console.log(canvas_height)

    scale = canvas_width/space_width

    svg = d3.select("body").append("svg")
        .attr("width", canvas_width)
        .attr("height", canvas_height)

    this.draw = function(data){

        habitats = data.habitats
        animals = data.animals

        // console.log(habitats)
        background = svg.append("g")

        background.selectAll("circle")
            .data(habitats)
            .enter()
            .append("circle")
            .attr("cx", (d) => {return d.x * scale})
            .attr("cy", (d) => {return d.y * scale})
            .attr("r", (d) => {return d.radius * scale})
            .attr("fill", "grey")


        active = svg.append("g")

        active.selectAll("circle")
            .data(habitats)
            .enter()
            .append("circle")
            .attr("cx", (d) => {return d.x * scale})
            .attr("cy", (d) => {return d.y * scale})
            .attr("r", (d) => {return d.radius * scale * d.percent})
            .attr("fill", (d) => {return d3.interpolateLab("red", "green")(d.geneticDiversity)})

        // console.log(animals)

        animals = svg.append("g")
            .attr("class", "animals")
            .selectAll("circle")
            // .append("circle")
            .data(animals)
            .enter()
            .append("circle")
            .attr("cx", (d) => {return d.x * scale})
            .attr("cy", (d) => {return d.y * scale})
            .attr("r", 5)
            .attr("fill", "green")
            .attr("r", (d) => {
                // console.log(d)
                return 5
            })

    }

    this.drawAnimals = function(animals){
        // console.log(animals)
        animals = svg.append("g")
            .attr("class", "animals")

        animals.selectAll("circle")
            .data(animals)
            .enter()
            .append("circle")
            .attr("cx", (d) => {return d.x * scale})
            .attr("cy", (d) => {return d.y * scale})
            .attr("r", 5)
            .attr("fill", "green")
            .attr("r", (d) => {
                // console.log(d)
                return 5
            })
    }


    this.render = function(data){
        // console.log(data)
        if(currentFrame % drawEvery == 0){
            console.log("draw")
            $('svg').empty()
            this.draw(data)
        } else {
            console.log("skip")
        }

        currentFrame += 1

        // this.drawHabitats(data.habitats)
        // this.drawAnimals(data.animals)
    }

    this.reset = function(){

        console.log("reset")
        $('svg').empty();

    }

}
