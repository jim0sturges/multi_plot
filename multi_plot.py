def multi_plot(df):
    '''
    purpose: will takin pandas dataframe and plot the columns using the index as the x axis
             and the column values as the y axis
    input:   - a data frame with numeric values in columns
             - cmap: dictionary used for small number of graphs
    output:  a dictionary of the containing the column name and a tuple of graph position
                 in a graph matrix (e.g. (0,0) or (1,3))
    '''
    import pandas as pd
    #%matplotlib inline
    import matplotlib.pylab as plt
    from IPython.display import display
    import matplotlib.dates as mdates
################################################################################    
    def map_it(col_list,nrows,ncols):
        '''
        purpose: This function will accept a list of column names and calculate the positioning
                 of each graph in a 2 wide or 3 wide (predetermined) layout
        input:   - a list of column names
                 - cmap: dictionary used for small number of graphs
        output:  a dictionary of the containing the column name and a tuple of graph position
                     in a graph matrix (e.g. (0,0) or (1,3))
        ''' 
        graph_loc={}
        row=0; col=0
        ncols=ncols-1;nrows=nrows-1
        for name in col_list:
            graph_loc[name]=(row,col)
            if col <= ncols-1:
                col=col+1
            else:
                if row < nrows:
                    row=row+1
                    col=0
        return graph_loc 
  ########################################################################  
    def nrow_ncols(col_list, small = {1:[1,1],2:[1,2],3:[2,2],4:[2,2]}):
        '''
        purpose: This function will accept a list of column names and calculate the number
                 of rows and columns needed for a graph matrix. Below 4 graphs it will use a
                 mix of 3 and 4 graphs wide. Over four columns it will us 3 graphs wide.
        input:   - col_list: list of columns to be graphed
                 - cmap: dictionary used for small number of graphs             - 
        output:  the number of rows and the number of columns needed for graphing. 
        call:    nrows,ncols=nrow_ncols(col_list)
        ''' 
        import math   
        len_cols=len(col_list)

        if len_cols in small.keys():
            ncols=small[len_cols][0]
            nrows=small[len_cols][1]
        else:
            nrows=math.ceil(len_cols/3)
            ncols=3
        return(nrows,ncols)
    ############################################################################
    ################ main plot routine #########################################
    col_list=list(df.columns)
    nrows,ncols=nrow_ncols(col_list)
    graph_loc=map_it(col_list,nrows,ncols)

    height=nrows*3.5
    fig,axes = plt.subplots(nrows=nrows, ncols=ncols, figsize= (15,height))
    #axes.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

    fig.subplots_adjust(hspace=.8)
    fig.subplots_adjust(wspace=0.3)

    for col in col_list:
        # The single row has to handled separately. Matplotlib does not care for [0,n]
        # arrays. it throws an error unless handled as a [n] array
        if nrows==1:
            df[col].plot(ax=axes[graph_loc[col][1]]);
            axes[graph_loc[col][1]].set_title(col,fontsize=15);
            axes[graph_loc[col][1]].set_xlabel('xxxx',fontsize=20, color='b')
            axes[graph_loc[col][1]].set_ylabel('yyyy',fontsize=20)
            axes[graph_loc[col][1]].fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
        else:
            df[col].plot(ax=axes[graph_loc[col][0],graph_loc[col][1]]);
            axes[graph_loc[col][0],graph_loc[col][1]].set_title(col,fontsize=15);
            axes[graph_loc[col][0],graph_loc[col][1]].set_xlabel('',fontsize=20, color='r');
            for tick in axes[graph_loc[col][0],graph_loc[col][1]].get_xticklabels():
                tick.set_rotation(45)
                
            axes[graph_loc[col][0],graph_loc[col][1]].set_ylabel('close',fontsize=20);
            axes[graph_loc[col][0],graph_loc[col][1]].fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
            
    plt.show()
    return
