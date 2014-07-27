<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="resources/hex.css"></link>
    <script src="http://code.jquery.com/jquery-latest.js"></script>
</head>
<body bgcolor="{{tile['color']}}">

<h1>{{user['user']}}</h1>
<h2>{{tile['type']}}</h2>
<p>Currently Located at {{user['latitude']}}, {{user['longitude']}}</p>
<div id="resources">
    <ul>
    % if 'stone' in tile:
        <li>Stone: {{tile['stone']}}</li>
    % end
    % if 'wood' in tile:
        <li>Wood: {{tile['wood']}}</li>
    % end
    % if 'food' in tile:
        <li>Food: {{tile['food']}}</li>
    % end
    </ul>
</div>


<div id="map" style="float: left; width: 340px;height:340px;background: grey">
    <div class="hex-row">
        <div class="empty"></div>
        % if 0 in map and 1 in map[0]:
        <div data-role="page" data-direction="north" class="direction hex even" style="margin-top: 15px;">
            <div class="left" style="border-right:30px solid {{map[0][1]['color']}}"></div>
            <div class="middle" style="background:{{map[0][1]['color']}}"></div>
            <div class="right" style="border-left:30px solid {{map[0][1]['color']}}"></div>
        </div>
        % else:
        <div class="empty"></div>
        % end
        <div class="empty"></div>
    </div>
    <div class="hex-row">
        % if -1 in map and 0 in map[-1]:
        <div data-direction="northwest" class="direction hex" style="color:{{map[-1][0]['color']}}">
            <div class="left" style="border-right:30px solid {{map[-1][0]['color']}}"></div>
            <div class="middle" style="background:{{map[-1][0]['color']}}"></div>
            <div class="right" style="border-left:30px solid {{map[-1][0]['color']}}"></div>
        </div>
        % else:
        <div class="empty"></div>
        % end
        <div class="hex even">
            <div class="left" style="border-right:30px solid {{tile['color']}}"></div>
            <div class="middle" style="background:{{tile['color']}}"></div>
            <div class="right" style="border-left:30px solid {{tile['color']}}"></div>
        </div>
        % if 1 in map and 1 in map[1]:
        <div data-direction="northeast" class="direction hex">
            <div class="left" style="border-right:30px solid {{map[1][1]['color']}}"></div>
            <div class="middle" style="background:{{map[1][1]['color']}}"></div>
            <div class="right" style="border-left:30px solid {{map[1][1]['color']}}"></div>
        </div>
        % else:
        <div class="empty"></div>
        % end
    </div>
    <div class="hex-row">
        % if -1 in map and -1 in map[-1]:
        <div data-direction="southwest" class="direction hex">
            <div class="left" style="border-right:30px solid {{map[-1][-1]['color']}}"></div>
            <div class="middle" style="background:{{map[-1][-1]['color']}}"></div>
            <div class="right" style="border-left:30px solid {{map[-1][-1]['color']}}"></div>
        </div>
        % else:
        <div class="empty"></div>
        % end
        % if 0 in map and -1 in map[0]:
        <div data-direction="south" class="direction hex even">
            <div class="left" style="border-right:30px solid {{map[0][-1]['color']}}"></div>
            <div class="middle" style="background:{{map[0][-1]['color']}}"></div>
            <div class="right" style="border-left:30px solid {{map[0][-1]['color']}}"></div>
        </div>
        % else:
        <div class="empty"></div>
        % end
        % if 1 in map and 0 in map[1]:
        <div data-direction="southeast" class="direction hex">
            <div class="left" style="border-right:30px solid {{map[1][0]['color']}}"></div>
            <div class="middle" style="background:{{map[1][0]['color']}}"></div>
            <div class="right" style="border-left:30px solid {{map[1][0]['color']}}"></div>
        </div>
        % else:
        <div class="empty"></div>
        % end
    </div>
</div>

<form id="move" action="/move" method="post">
    <input type='hidden' name='user_id' value="{{user['_id']}}"/>
    <input id="direction" type='hidden' name='direction' />
</form>

<script>
    $( document ).ready(function() {
        $('div.direction').click(function() {
            $("#direction").val($(this).data("direction"));
            $("#move").submit();
        });
    });
</script>

</body>
</html>