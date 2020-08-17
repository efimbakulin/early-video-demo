TEMPLATE = """
<html>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">

<body>

    <div class="container-fluid height=680px">
        <div class="row">
            <div class="col-md-8">
                <iframe style="width:900px; height:680px;" allowfullscreen src="http://localhost:8080/channel/{{channel_id}}/embed.html?{{streaming_qs}}"></iframe>
            </div>
            {% for id, c in channels.items() %}
            <div class="col-md-2  height=680px">

                    <div>
                    <h5 class="mb-0">
                        {{c['name']}}
                    </h5>
                    {% for p in c['programme'] %}
                    <div class="list-group-item">
                        <a href="?c={{c['id']}}&p={{loop.index-1}}"> {{ p['title'] }}</a>
                        <br/>
                        {{ render_show_time (p) }}
                    </div>
                    {% endfor%}
                    </div>
            </div>
            {% endfor %}
        </div>
    </div>
    </div>
</body>

</html>
"""
