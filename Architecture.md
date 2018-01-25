# Architecture

## Device-Gateway-Cloud

    ------------
    | Device1  |-----
    ------------    |                                                               |-----Mobile Applications
                    |                                ----|----------|----           |
    ------------    |       -------------           |                    |          |-----Web Applications
    | Device2  |------------| Gateway   |---------|      Cloud Infra        |-------|
    ------------    |       -------------           |                    |          |-----Big Data Analytics
                    |                                ----|----------|----           |
    ------------    |                                                               |-----Real-Time data streams          
    | Device3  |-----
    ------------