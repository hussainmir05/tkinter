=root)
        canvas.draw()
        canvas.get_tk_widget().place(x=350,y=150,width=1000,height=400)
        self.root.after(5000, self.create_graph)
        